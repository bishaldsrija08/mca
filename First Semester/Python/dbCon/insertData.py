import connection

mycursor = connection.con.cursor()
mycursor.execute("INSERT INTO students (name, age) VALUES ('John Doe', 25)")
connection.con.commit()
connection.con.close()
print("Data inserted successfully.")