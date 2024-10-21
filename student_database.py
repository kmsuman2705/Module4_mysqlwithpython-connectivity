import mysql.connector

# Step 1: Connection setup karein
conn = mysql.connector.connect(
    host="localhost",  # Agar remote MySQL ho, toh host address daalein
    user="root",       # MySQL ka username
    password="your_password",  # Root password ya jo aapne setup kiya ho
    database="student_db"
)

cursor = conn.cursor()

# Step 2: Student ko insert karne ka function
def insert_student(name, age, grade):
    query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    cursor.execute(query, values)
    conn.commit()
    print(f"Student {name} added successfully!")

# Step 3: Sabhi students ko fetch karne ka function
def fetch_students():
    query = "SELECT * FROM students"
    cursor.execute(query)
    results = cursor.fetchall()

    for student in results:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")

# Example usage
insert_student('Alice', 20, 'A')
insert_student('Bob', 19, 'B')

print("\nList of students:")
fetch_students()

# Close the connection
cursor.close()
conn.close()
