import psycopg2
import random

conn=psycopg2.connect(host="localhost",dbname="postgres",user="postgres",password="Navin@2002",port="5432")
cur=conn.cursor()


cur.execute(
"""
CREATE TABLE if not exists public.some(
id SERIAL PRIMARY KEY,
name VARCHAR(255),
age INT,
dept VARCHAR(255)
);
"""
)

names=["navin","ashok","swami","nathan","john","smith"]
ages=list(range(20,30))
depts=["IT","FINANCE","MATHS"]
for i in range(150):
    query= "insert into public.some(name,age,dept) values ('{}',{},'{}')".format(random.choice(names),random.choice(ages),random.choice(depts))
    cur.execute(query)




conn.commit()
cur.close()
conn.close()