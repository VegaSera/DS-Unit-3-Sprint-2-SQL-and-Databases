import sqlite3

#---------------------------------------------
#---------------------------------------------
# Part 2 - Northwind Database
#---------------------------------------------
#---------------------------------------------

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

def run_query(query):
    return curs.execute(query).fetchall()

#---------------------------------------------
#What are the 10{num} most expensive items per unit price?
#---------------------------------------------
num = 10 # Number requested can be easily changed now.
q1_query = f"""
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT {num}
"""

q1_result = run_query(q1_query)
print(f"These are the top {num} most expensive items.")
for i in range(num):
    print(f"{q1_result[i][0]} - Price: {q1_result[i][1]}")
print('\n') #Newline to separate from the next question. Purely stylistic

#Printed Results
""" 
These are the top 10 most expensive items.
Côte de Blaye - Price: 263.5
Thüringer Rostbratwurst - Price: 123.79
Mishi Kobe Niku - Price: 97
Sir Rodney's Marmalade - Price: 81
Carnarvon Tigers - Price: 62.5
Raclette Courdavault - Price: 55
Manjimup Dried Apples - Price: 53
Tarte au sucre - Price: 49.3
Ipoh Coffee - Price: 46
Rössle Sauerkraut - Price: 45.6
"""

#---------------------------------------------
#What is the average age of an employee at the time of their hiring?
#---------------------------------------------
q2_query = """
SELECT ROUND(AVG((strftime('%Y', HireDate) - strftime('%Y', BirthDate)) - (strftime('%m-%d', HireDate) < strftime('%m-%d', BirthDate))), 2)
FROM Employee
"""
q2_result = run_query(q2_query)
print("What is the average age of an employee at the time of hiring?")
print(f"Employees are {q2_result[0][0]} years old at the time of hiring on average.\n")

#Printed Results
"""
What is the average age of an employee at the time of hiring?
Employees are 36.78 years old at the time of hiring on average.
"""

#---------------------------------------------
#(Stretch) How does the average age of employee at hire vary by city?
#---------------------------------------------



#---------------------------------------------
#---------------------------------------------
# Part 3 - Sailing the Northwind Seas
#---------------------------------------------
#---------------------------------------------

#---------------------------------------------
# What are the ten most expensive items (per unit price) in the database and their suppliers?
#---------------------------------------------

num = 10  #Setting for easy changing once again.
q4_query = f"""
SELECT ProductName, UnitPrice, CompanyName
FROM Product
LEFT JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT {num}
"""

q4_result = run_query(q4_query)
print(f"These are the top {num} most expensive items, and their supplier.")
for k in range(num):
    print(f"{q4_result[k][0]} - Price: {q4_result[k][1]} - Supplier: {q4_result[k][2]}")
print('\n') #Newline to separate from the next question

#Printed Results
"""
These are the top 10 most expensive items, and their supplier.
Côte de Blaye - Price: 263.5 - Supplier: Aux joyeux ecclésiastiques
Thüringer Rostbratwurst - Price: 123.79 - Supplier: Plutzer Lebensmittelgroßmärkte AG
Mishi Kobe Niku - Price: 97 - Supplier: Tokyo Traders
Sir Rodney's Marmalade - Price: 81 - Supplier: Specialty Biscuits, Ltd.
Carnarvon Tigers - Price: 62.5 - Supplier: Pavlova, Ltd.
Raclette Courdavault - Price: 55 - Supplier: Gai pâturage
Manjimup Dried Apples - Price: 53 - Supplier: G'day, Mate
Tarte au sucre - Price: 49.3 - Supplier: Forêts d'érables
Ipoh Coffee - Price: 46 - Supplier: Leka Trading
Rössle Sauerkraut - Price: 45.6 - Supplier: Plutzer Lebensmittelgroßmärkte AG
"""

#---------------------------------------------
# What is the largest category (by number of unique products in it)?
#---------------------------------------------

num = 1 #Getting largest for now, but can get N largest if desired.
q5_query = f"""
SELECT CategoryName, COUNT(*)
FROM Product
LEFT JOIN Category ON Product.CategoryId = Category.Id
GROUP BY CategoryName
ORDER BY COUNT(*) DESC
LIMIT {num}
"""

q5_result = run_query(q5_query)
print(f"Largest {num} Categories by unique products")
for j in range(num):
    print(f"{q5_result[j][0]} - {q5_result[j][1]} unique items")

#Printed Results
"""
Largest 1 Categories by unique products
Confections - 13 unique items
"""

#---------------------------------------------
#(Stretch) Who's the employee with the most territories? Use TerritoryId (not name, region, or other fields) as the unique identifier for territories.
#---------------------------------------------


#---------------------------------------------
#---------------------------------------------
# Part 4 - Questions and Answers
#---------------------------------------------
#---------------------------------------------


#---------------------------------------------
#In the Northwind database, what is the type of relationship between the Employee and Territory tables?
#---------------------------------------------
"""
There's a One to One relationship between Employees and EmployeeTerritories, via the EmployeeID columns. 
There's a One to One relationship between EmployeeTerritories and Territories, via the Territory ID.
However there is a One to Many relationship between Employees and Territories, as one employee can (and often does) have multiple territories assigned to them.
"""

#---------------------------------------------
#What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
#---------------------------------------------
"""
It is my understanding that document stores like MongoDB are mostly appropriate in two cases. 
The first is when you're planning on dealing with currently unstructured data, or where the structure is yet to be 
finalized but data still must be stored, such as in a prototyping phase. 
The second is when relational databases are too slow to facilitate the sheer amount of data provided to it. This
typically happens when reaching the regime of the hundreds of millions of rows.
"""

#---------------------------------------------
#What is "NewSQL", and what is it trying to achieve?
#---------------------------------------------
"""
NewSQL is attempting to bridge the gap between Relational Databases and NoSQL Document Stores, trying to provide 
essentially the best of both worlds.
It is a relational database at its core, with a focus on the scalability of Document Stores while 
also conforming to ACID, to ensure the integrity of its data.
"""