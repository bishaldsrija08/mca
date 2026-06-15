import connection

mycursor = connection.con.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydb_mca")
print("Database created successfully.")