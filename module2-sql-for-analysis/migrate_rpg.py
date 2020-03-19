import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
import psycopg2
from sqlalchemy import create_engine

filepath = os.path.join(os.path.dirname(__file__),"..","module1-introduction-to-sql","")
#filepath = 'C:/Users/Vega/Documents/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/' # Original Filepath
conn = sqlite3.connect(filepath + 'rpg_db.sqlite3')

rpg_tables = ['armory_item', 'armory_weapon','charactercreator_character','charactercreator_character_inventory',
               'charactercreator_cleric','charactercreator_fighter','charactercreator_mage','charactercreator_necromancer',
               'charactercreator_thief']

dfs = []
for table in rpg_tables:
    dfs.append(pd.read_sql(f"SELECT * FROM {table};", conn))


load_dotenv()
URL = os.getenv('URL')
engine = create_engine(URL)

#Didn't work, Google says to use sqlalchemy
#psyc_conn = psycopg2.connect(dbname=dbname, user=dbuser, host=dbhost, password=dbpass)

for i in range(len(rpg_tables)):
    dfs[i].to_sql(rpg_tables[i], engine,
                            if_exists='replace', method='multi')