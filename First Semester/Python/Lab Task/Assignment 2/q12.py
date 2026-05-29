# Create a file with name Sample.txt and write some contents into it. Also read the contents of the file. Also copy the contents of the file to another file with name Copy.txt.

with open("Sample.txt", "w") as file:
    file.write("Hello Bishal!\nThis is a sample file.\nIt contains some text data.")
    

with open("Sample.txt", "r") as file:
    contents = file.read()
    print("Contents of Sample.txt:")
    print(contents)
    
with open("Copy.txt", "w") as copy_file:
    copy_file.write(contents)
    
print("Contents have been copied to Copy.txt")