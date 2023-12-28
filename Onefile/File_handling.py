# File handling in Python involves reading from and writing to files.
# Python provides built-in functions and methods for performing these operations. 
# Here's an overview of file handling in Python:
with open("myFile.txt", 'r') as file:# reading the file
	print(file.read())
print(file.closed)
#writing the file format the file enter new one
txt ="This is newly added text" # text for write 
with open("myFile.txt", 'w') as file:# reading the file
	file.write(txt)
print(file.closed)
#append the text without data erase 
with open("myFile.txt", 'a') as file:
	file.write(" append behind the new text ")