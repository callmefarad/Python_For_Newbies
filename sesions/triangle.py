# write a program that displayse a right angle triangle
# ALGORITHM TO PRINT THE PATTERN USING FOR LOOP IN PYTHON
# the algorithm depends on towo for loops where the first for loop is the number of rows and the second for loop is the number of column
# 1. accepts the number of rows from a user using input() function or decide the size of a pattern.
# 2. iterate the number of rows using outer for loop and range() function.
# 3. next, the inner loop or nested for loop to handle the number of columns. inner loop iteration depends on the values of the outer loop.
# 4. print start, number, asteriks, pyramid and diamond pattern using the print() function.
# 5. add a new line after each row, i.e. agter each iteration of outer for loop so you can display pattern appropriately.


# ask for user input for the number of rows
userinput_row = input("Enter the number of weidth of the right angle trinagle: ")
# a for loop that iterate on the number of weidth provided
for num in range(int(userinput_row)):
    # nested for loop (height/column) that iterate on the number of outer for loop (weight/row)
    for i in range(num):
        # print an asteriks(*) to display the iterations of the weidth and height
        #print('*', end=" ")
        print(num, end=' ')
        # print a new line to make the presentation look good
    print(' ')