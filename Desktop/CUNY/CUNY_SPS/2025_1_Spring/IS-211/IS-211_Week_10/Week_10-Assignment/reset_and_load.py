import sqlite3
import os

# Remove old database if exists
if os.path.exists('pets.db'):
    os.remove('pets.db')

# Create new database
conn = sqlite3.connect('pets.db')
c = conn.cursor()

# Create tables
c.execute("""CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)""")

c.execute("""CREATE TABLE pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
)""")

c.execute("""CREATE TABLE person_pet (
    person_id INTEGER,
    pet_id INTEGER
)""")

# Insert data
people = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]

pets = [
    (1, 'Rusty', 'Dalmatton', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

person_pet = [
    (1, 1), (1, 2), (2, 3),
    (2, 4), (3, 5), (4, 6)
]

c.executemany("INSERT INTO person VALUES (?,?,?,?)", people)
c.executemany("INSERT INTO pet VALUES (?,?,?,?,?)", pets)
c.executemany("INSERT INTO person_pet VALUES (?,?)", person_pet)

conn.commit()
conn.close()
print("Database reset and data loaded successfully!")