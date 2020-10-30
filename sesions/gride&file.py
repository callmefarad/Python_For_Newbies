# creating a grid list and reading of file
#grid list
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col, end='')
print('\n'*2)


# file operation
list = open("student-list.txt", "r")
print(list.read())
list.close()

list2 = open("student-list.txt", "r")
print(list2.readline())
list2.close()

list3 = open("student-list.txt", "r")
print(list3.readlines())
list3.close()

list4 = open("student-list.txt", "r")
for rows in list4.readlines():
    print(rows, end='')
list4.close()

list5 = open("student-list.txt", "r")
for rows in list5.readlines()[3]:
    print(rows, end='')
list4.close()