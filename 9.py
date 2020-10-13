# seek(),tell()



#  we are going to study why there is a need for tell() and seek() functions and how we can use them? 
# tell()
# When we are working with python files, there are several ways to present the output of a program, it could be in human-readable form or binary form, or we use read() function with specified sie to read some data.

# What if we want to know the position of the file(read/write) pointer.
# For this purpose, we use the tell() function. f.tell() returns an integer giving the file pointer current position in the file represented as a number of bytes. File Pointer/File Handler is like a cursor, which defines from where the data has to be read or written in the file. Sometimes it becomes important for us to know the position of the File Pointer. With the help of tell(), this task can be performed easily 

# Description:
# Syntax:  seek()
# Parameters Required: No parameters are required.
# Return Value:  seek() function returns the current position of the file pointer within the file.




f = open("myfile.txt", "r")
print(f.readline() )
print(f.tell())



f = open("myfile.txt", "r")
f.seek(5)
print( f.readline() )





f = open("harry.txt")
f.seek(11)
print(f.tell())
print(f.readline())
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()
  
