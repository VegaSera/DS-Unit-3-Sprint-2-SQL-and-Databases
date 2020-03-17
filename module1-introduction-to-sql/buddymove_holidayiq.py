import pandas as pd
import os
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
#if not os.path.exists('buddymove_holidayiq.sqlite3'):
df.to_sql('buddymove_holidayiq', conn, if_exists="replace")



#Row count
q1_query = """
SELECT COUNT(*)
FROM buddymove_holidayiq
"""

q1_result = curs.execute(q1_query).fetchall()
print(f"Has {q1_result[0][0]} rows.")



#How many users reviewed 100 in nature and 100 in shopping
q2_query = """
SELECT COUNT(*) 
FROM buddymove_holidayiq
WHERE buddymove_holidayiq.Nature >= 100 AND buddymove_holidayiq.Shopping >= 100
"""
q2_result = curs.execute(q2_query).fetchall()
print(f"{q2_result[0][0]} users have reviewed at least 100 in both Nature and Shopping.")