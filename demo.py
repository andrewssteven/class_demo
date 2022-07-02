import psycopg2

connection = psycopg2.connect(database = "example", user = "postgres", password = "12345")

cursor = connection.cursor()


cursor.execute('INSERT INTO table2 (id, completed) VALUES (5, true);')

cursor.execute('SELECT * FROM table2;')
result = cursor.fetchall()

print(result)

connection.commit()

connection.close()
cursor.close()