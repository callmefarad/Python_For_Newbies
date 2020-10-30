# Python File Operation
# The following operation can be perform on a file using python.
# Read, Write, Update and



# Open a file and read all data. With this operation, the data can't be altered.
list = open("student-list.txt", "r")
print(list.read())
list.close()


# Read one line of data in the file
list2 = open("student-list.txt", "r")
print(list2.readline())
list2.close()

# Reads all the lines in the file and displaying them horizontally by default
list3 = open("student-list.txt", "r")
print(list3.readlines())
list3.close()

# Using for loop to perform read operation(read all the lines) in a file
list4 = open("student-list.txt", "r")
for rows in list4.readlines():
    print(rows, end='')
list4.close()

# Reading a particular line using for loop
list5 = open("student-list.txt", "r")
for rows in list5.readlines()[3]:
    print(rows, end='')
list4.close()