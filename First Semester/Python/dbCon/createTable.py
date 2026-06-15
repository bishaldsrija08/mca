import connection

mycursor = connection.con.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")
print("Table created successfully.")