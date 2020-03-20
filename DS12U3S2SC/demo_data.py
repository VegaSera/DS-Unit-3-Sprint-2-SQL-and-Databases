import sqlite3

#---------------------------------------------
# Part 1 - Making and Populating a Database
#---------------------------------------------


demo_connect = sqlite3.connect('demo_data.sqlite3')
demo_curs = demo_connect.cursor()

def run_query(query):
    return demo_curs.execute(query).fetchall()

demo_table_create_query = """
CREATE TABLE IF NOT EXISTS demo (
s VARCHAR PRIMARY KEY,
x INT,
y INT)

INSERT INTO demo (s,x,y)
VALUES
('g', 3, 9),
('v', 5, 7),
('f', 8, 7)
"""

#Commented the below out to prevent duplicate insert statements while testing queries
#demo_curs.execute(demo_table_create_query)
demo_connect.commit()

#How many rows:
q1_query ="""
SELECT COUNT(*)
FROM demo
"""

q1_result = run_query(q1_query)
print(f"Our demo table has {q1_result[0][0]} rows.")

#How many rows where both x and y are at least 5?
q2_query = """
SELECT COUNT(*)
FROM demo
WHERE x >= 5 AND y >= 5
"""

q2_result = run_query(q2_query)
print(f"There are {q2_result[0][0]} rows where columns x and y are both at least 5.")

#How many unique values of y are there?
q3_query = """
SELECT COUNT(Distinct y)
FROM demo
"""

q3_result = run_query(q3_query)
print(f"There are {q3_result[0][0]} distinct values of y.")