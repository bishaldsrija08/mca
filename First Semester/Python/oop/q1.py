"""
HW:
Create a class Book that contains instance attribute isbn, author, price. Use initializer to initialize the value of special str function to display the object values. Perfom equal to operator overloading to check whether a two book has same isbn or not.
"""

class Book:
    def __init__(self, isbn, author, price):
        self.isbn = isbn
        self.author = author
        self.price = price
        
    def __str__(self):
        return f"ISBN: {self.isbn}, Author: {self.author}, Price: {self.price}"
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False
    
# Example usage
book1 = Book("12345", "Author A", 29.99)
book2 = Book("123456", "Author B", 39.99)
print(book1)  # Output: ISBN: 12345, Author: Author A, Price: 29.99
print(book2)  # Output: ISBN: 12345, Author: Author B,

print(book1 == book2)  # Output: True