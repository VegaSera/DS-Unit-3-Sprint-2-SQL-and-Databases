import pandas as pd
import os
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv


load_dotenv()
dbname=os.getenv('DB_NAME')
dbuser=os.getenv('DB_USER')
dbpassword=os.getenv('DB_PASSWORD')
dbhost=os.getenv('DB_HOST')



conn = psycopg2.connect(dbname=dbname, user=dbuser,
                        password=dbpassword, host=dbhost)
print("Connection: ", conn)
curs = conn.cursor()


create_table = """
CREATE TABLE IF NOT EXISTS titanic
(id SERIAL PRIMARY KEY,
Survived INTEGER,
Pclass INTEGER,
Name VARCHAR,
Sex VARCHAR,
Age FLOAT,
Siblings_Spouses INTEGER,
Parents_Children INTEGER,
Fare FLOAT);
"""
curs.execute(create_table)

curs.execute("SELECT * FROM titanic;")
result = curs.fetchall()

if len(result) == 0:
    df = pd.read_csv('titanic.csv')
    insert_query = "INSERT INTO titanic (Survived, Pclass, Name, Sex, Age, Siblings_Spouses, Parents_Children, Fare) VALUES %s"
    rows = list(df.itertuples(index=False, name=None))
    execute_values(curs, insert_query, rows)

conn.commit()

