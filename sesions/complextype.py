# showing complex type representation
# declaring a variable name complex_number and the value 20i
complex_number = 40 + 2j
# displaying the complex number
print("This is python complex number")
print(complex_number)

# displaying python data type of the output
print("This is python data type representation of complex number:")
print(type(complex_number))


print("\n")
# we can also get the complex, real and imaginary number from in-built
# functions
# importing the class
import cmath, math

# declaring the variables
y = 30
z = (20 + 2j)

print("The real number is: ", y.real, end="\n")
print("The complex number is: ", complex(z), end="\n")
print("The imaginary number is: ", y.imag)