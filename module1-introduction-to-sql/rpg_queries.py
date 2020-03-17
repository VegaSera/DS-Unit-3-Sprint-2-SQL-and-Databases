import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


def run_query(query):
    return curs.execute(query).fetchall()

#Q1 - How many characters are there
q1_query = """
SELECT COUNT(*)
FROM charactercreator_character
"""

q1_result = run_query(q1_query)
print(f"Q1 - How many characters are there?\nThere are {q1_result[0][0]} total characters. \n")

#Q2 - How many of each specific subclass?
q2_query = """
SELECT
	(SELECT COUNT(*) FROM charactercreator_fighter) as fighter_count,
	(SELECT COUNT(*) FROM charactercreator_mage) as mage_count,
	(SELECT COUNT(*) FROM charactercreator_thief) as thief_count,
	(SELECT COUNT(*) FROM charactercreator_cleric) as cleric_count,
	(SELECT COUNT(*) FROM charactercreator_necromancer) as necro_count
"""

q2_result = run_query(q2_query)
print(f"Q2 - How many of each specific subclass?\nThere are {q2_result[0][0]} fighters, {q2_result[0][1]} mages,"
      f" {q2_result[0][2]} thieves, {q2_result[0][3]} clerics, and {q2_result[0][4]} spooky necromancers, \n")

#Q3 - How many total items
q3_query = """
SELECT
	COUNT(*) FROM armory_item
"""

q3_result = run_query(q3_query)
print(f"Q3 - How many total items?\nThere are a total of {q3_result[0][0]} items. \n")

#Q4 - How many of the items are weapons
q4_query = """
SELECT COUNT(*) 
from armory_item
JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
	
"""

q4_result = run_query(q4_query)
print(f"Q4 - How many of the items are weapons?\n{q4_result[0][0]} of the items are weapons.\n")

#Q5 - How many items does each character have? Return first 20 rows
q5_query = """
SELECT character_id, COUNT(item_id)
from charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
"""

q5_result = run_query(q5_query)
print(f"Q5 - How many items does each character have?\n The first character has {q5_result[0][1]} items.\n"
      f"The second has {q5_result[1][1]} items. \nThe rest are as follows\n",q5_result,"\n")
#Could have done a for loop to cycle through the results and format them nicely, however it would take up too much space.

#Q6 - How many weapons does each character have? Return first 20 rows.
q6_query = """
SELECT character_id, COUNT(item_id)
from charactercreator_character_inventory
LEFT JOIN armory_weapon on charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY character_id
LIMIT 20
"""

q6_result = run_query(q6_query)
print(f"Q6 - How many weapons does each character have?\n The first character has {q6_result[0][1]} weapons.\n"
      f"The second has {q6_result[1][1]} weapons. \nThe rest are as follows\n",q6_result,"\n")

#Q7 - On average, how many items does each character have?
q7_query = """
SELECT round(avg(item_count), 2)
FROM (SELECT count(id) as item_count
	FROM charactercreator_character_inventory
	GROUP BY character_id)
"""
q7_result = run_query(q7_query)
print(f"Q7 - On average, how many items does each character have?\nCharacters have {q7_result[0][0]} items on average\n")

#Q8 - On average, how many weapons does each character have?
q8_query = """
SELECT
    round(avg(weapon_count), 2)
FROM
    (
        SELECT
            character_id,
            count(item_ptr_id) as weapon_count
        FROM
            charactercreator_character_inventory
            JOIN armory_weapon on charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
        GROUP BY character_id)
"""

q8_result = run_query(q8_query)
print(f"Q8 - On average, how many weapons does each character have?\nCharacters have {q8_result[0][0]} weapons on average\n")