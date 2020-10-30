# compute a multiplicatication table from the user entry.

#creating reuseable funtions
def copywrite():
    print("Copywrite: Ubani U. Friday")

def footer():
    print("#" * 40)

def multiplicationTable(entry1, entry2):
    for i in range(1, int(table_lenght)+1):
        print(int(table_value), "x", i, "=", int(table_value) * i)

# the main program
table_value = input("Enter your prefered value: ")
table_lenght = input("Enter the length of your table: ")

multiplicationTable(table_value, table_lenght)
footer()
print("That's the multiplication table for: ", table_value)
footer()
copywrite()
