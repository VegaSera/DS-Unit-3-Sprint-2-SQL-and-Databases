import pymongo
import os
from dotenv import load_dotenv
import sqlite3

"""
I'll be honest, I did not enjoy working with mongo. There doesn't seem to be a way for me to simply transfer over a whole database
because the syntax requires me to put the collection in as db._____, which doesn't seem like I can simply modify with code.
"""

load_dotenv()
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("CLUSTER_NAME", default="OOPS")


client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority")



filepath = os.path.join(os.path.dirname(__file__),"..","module1-introduction-to-sql","")

DB_FILEPATH = 'rpg_db.sqlite3'
connect = sqlite3.connect(filepath + 'rpg_db.sqlite3')
curs = connect.cursor()
print("CONNECT:", connect)

db = client.rpg_db


armory_query = """
SELECT * FROM armory_item
"""
get_armory = curs.execute(armory_query).fetchall()

collection = db.rpg_items
print("----------------")
print("COLLECTION:", type(collection), collection)
print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

for n in get_armory:
    collection.insert_one({
        "item_id":n[0],
        "name": n[1],
        "weight": n[2],
        "value": n[3]
    })
