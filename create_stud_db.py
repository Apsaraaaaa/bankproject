import sqlite3
import csv

conn = sqlite3.connect('student.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")
print(" Table created successfully!")


with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        cur.execute("INSERT INTO student (name, age, grade) VALUES (?, ?, ?)", row)
print(" Data inserted from CSV!")

print("\n All student records:")
cur.execute("SELECT * FROM student")
for row in cur.fetchall():
    print(row)


cur.execute("UPDATE student SET grade = ? WHERE name = ?", ("B+", "Gita"))
print("\n Updated Gita's grade to B+")


cur.execute("DELETE FROM student WHERE name = ?", ("Sita",))
print(" Deleted Sita from records")


cur.execute("INSERT INTO student (name, age, grade) VALUES (?, ?, ?)", ("Kiran", 23, "A"))
print(" Inserted new student: Kiran")


print("\n Final student records after CRUD:")
cur.execute("SELECT * FROM student")
for row in cur.fetchall():
    print(row)
    
conn.commit()
conn.close()
print("\n All operations completed!")