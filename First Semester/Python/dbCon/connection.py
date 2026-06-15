import mysql.connector as mysqlCon

con = mysqlCon.connect(
    host = "localhost",
    user= "root",
    password =""
)

print(con, "Db connection successfuylly.")