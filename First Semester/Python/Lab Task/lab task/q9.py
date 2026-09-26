import sqlite3

connection = sqlite3.connect("Product.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Product(
    PId INTEGER PRIMARY KEY,
    itemname TEXT,
    price REAL
)
""")

cursor.execute("DELETE FROM Product")

products = [
    (1, "Laptop", 75000),
    (2, "Keyboard", 1500),
    (3, "Monitor", 12000),
    (4, "Mouse", 800),
    (5, "Printer", 18000)
]

cursor.executemany(
    "INSERT INTO Product(PId, itemname, price) VALUES (?, ?, ?)",
    products
)

connection.commit()

print("Products with price more than Rs. 2000:")

cursor.execute("SELECT * FROM Product WHERE price > 2000")

for product in cursor.fetchall():
    print(product)

connection.close()