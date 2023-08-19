from flask import Flask
from flask_restful import Api,Resource
from flask_cors import CORS
from flask import jsonify
import psycopg2
app=Flask(__name__)
CORS(app)
#lis=[{"name":"navin","age":16},{"name":"ashok","age":14}]
lis=[("navin",1,"IT"),("ashok",2,"ECE")]
@app.route("/backend/<string:query>",methods=['GET'])
def some(query):
    conn=psycopg2.connect(host="localhost",dbname="postgres",user="postgres",password="Navin@2002",port="5432")
    cur=conn.cursor()
    print(query)
    cur.execute(query)
    result=cur.fetchall()
    print(result)
    conn.commit()
    cur.close()
    conn.close()



    return jsonify(result)
if __name__== "__main__":
    app.run(debug=True)
