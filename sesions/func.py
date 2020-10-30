# # declaring a function
# def dummy():
#     print("this is a dummy print.")
#
# # callin the function
# dummy()
#
# def add():
#     user1 = float(input('Enter your firstnumber: '))
#     user2 = float(input('Enter your secondnumber: '))
#     sum = user1 + user2
#     return sum
#
# # call the function
# add()

# x = 5
# def anything():
#     global x
#     x = 6
#     print(x * 2)
#
# anything()
# print(x)
#


# def greet(name, message):
#     print(name + " " + message)
# def greet(name, message):
#     return name + " " + message
#
# print(greet('ole', 'good morning'))
#
# def greet(name, message="goood morning"):
#     print( name + " " + message)
#
#
# greet("osazie", "welcome")

# def fruits(*fruitslist):
#     return fruitslist
#
# print(fruits('ola', 'sade', 'tolu'))


# # using a lamdda function
# square = lambda x, y: (x*x) - (y)
#
# print(square(4,4))

# root of an equation (b2 - 4ac)/(2a)
# equation_root = lambda a,b,c : -b((b*b - 4*a*c)/(2*a))
#
# a = float(input('Enter the value of a: '))
# b = float(input('Enter the value of b: '))
# c = float(input('Enter the value of c: '))
#
# # call the lamda function
# print(equation_root(a,b,c))


# a lambda function that performs the square of a number
# square = lambda x: x * y
# 
# user = float(input('number: '))
# print(square(user))

root = lambda a, b, c: ((a*a) + (b) -c)

x = float(input('a: '))
y = float(input('b: '))
z = float(input('c: '))

# call the function
print(root(x,y,z))




# a default function that performs the square of a number
# def square(x):
#     result = x * x
#     return result
# 
# u = float(input('number: '))
# print(square(u))









