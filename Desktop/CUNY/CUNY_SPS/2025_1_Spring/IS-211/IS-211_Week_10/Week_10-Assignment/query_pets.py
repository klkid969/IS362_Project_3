import sqlite3

conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

# Query to join person and pet data
cursor.execute("""
    SELECT person.first_name, person.last_name, pet.name, pet.breed, pet.age, pet.dead
    FROM person_pet
    JOIN person ON person_pet.person_id = person.id
    JOIN pet ON person_pet.pet_id = pet.id
    ORDER BY person.last_name
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()