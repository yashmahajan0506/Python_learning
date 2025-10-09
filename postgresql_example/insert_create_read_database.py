import psycopg2

conn = psycopg2.connect(
        dbname="emp",
        user="postgres",
        password="Yash@2102", 
        host="localhost",
        port="5432"
    )
cursor = conn.cursor()

insert_query = """
    INSERT INTO employees (name, dep, salary)
    VALUES (%s, %s, %s)
    """
records = [
        ('Yash', 'IT', 50000),
        ('Sujal', 'HR', 45000),
        ('Piyush', 'Finance', 55000)
    ]

cursor.executemany(insert_query, records)
conn.commit()
print(" Records inserted successfully!")

cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()
print(" Employee Records:")
for row in rows:
        print(row)

