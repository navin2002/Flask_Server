from flask import Flask
from flask_restful import Api,Resource
from flask_cors import CORS
from flask import jsonify
app=Flask(__name__)
CORS(app)
lis=[{"name":"navin","age":16},{"name":"ashok","age":14}]
@app.route("/backend/<string:query>",methods=['GET'])
def some(query):
    print(query)
    return jsonify(lis)
if __name__== "__main__":
    app.run(debug=True)
