import mysql.connector as mysqlCon

con = mysqlCon.connect(
    host = "localhost",
    user= "root",
    password ="",
    database = "mydb_mca"
)

mycursor = con.cursor()

print(con, "Db connection successfuylly.")