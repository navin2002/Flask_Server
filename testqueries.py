import psycopg2
query="select name,age from public.some where age>28"
conn=psycopg2.connect(host="localhost",dbname="postgres",user="postgres",password="Navin@2002",port="5432")
cur=conn.cursor()
cur.execute(query)
print(cur.fetchall())
conn.commit()
cur.close()
conn.close()