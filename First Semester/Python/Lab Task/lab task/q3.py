# Create and write to Sample.txt
with open("Sample.txt", "w") as file:
    file.write("Python is a high-level programming language.\n")
    file.write("It is easy to learn and widely used.\n")
    file.write("Python supports file handling.")

# Read Sample.txt
with open("Sample.txt", "r") as file:
    contents = file.read()

print("Contents of Sample.txt:")
print(contents)

# Copy contents to Copy.txt
with open("Copy.txt", "w") as file:
    file.write(contents)

print("Contents copied successfully to Copy.txt")