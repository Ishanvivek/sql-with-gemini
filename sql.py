import sqlite3
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

# SQL command to create the STUDENT table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25), 
    CLASS VARCHAR(25),
    SECTION VARCHAR(25), 
    MARKS INT
);
"""
cursor.execute(table_info)

# Generate 200 random data and insert into STUDENT table
for _ in range(200):  # 200 rows
    name = fake.first_name()
    class_name = random.choice(['Data Science', 'Web Development', 'Block Chain', 'AI', 'DevOps', 'Front End', 'Back End', 'Cloud Computing', 'Cyber Security', 'Machine Learning'])
    section = random.choice(['A', 'B', 'C'])
    marks = random.randint(70, 100)
    
    cursor.execute(f"INSERT INTO STUDENT values('{name}','{class_name}','{section}',{marks})")

# Print the inserted records
print("200 random records have been inserted.")

# Commit the transaction
connection.commit()

# Close the connection
connection.close()
