# importing our module
import math_modu

# displaying the sum of two numbers
result = math_modu.sum(2, 8)
print("\nThe sum of the two numbers 2 and 8 is: ", result)

# displaying the difference between two numbers
result2 = math_modu.sub(2, 8)
print("The difference between the two numbers 2 and 8 is: ", result2)

# displaying the division of two numbers
result3 = math_modu.div(2, 8)
print("The division of the two numbers 2 and 8 is: ", result3)

# displaying the multiplication of two numbers
firstnumber = input("Enter your first number: ")
secondnumber = input("Enter you second number: ")

# call the module
result4 = math_modu.mult(firstnumber, secondnumber)
print("The multiplication of the two numbers 2 and 8 is: ", result4)

