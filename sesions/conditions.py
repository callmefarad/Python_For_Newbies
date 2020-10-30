# if .. elif and else

# if condition
# if bool:
#     print('this is the body of the condition')
#
# print('a default value')

# write a program that check if the userinput is an even number
# declare the variable to hold userinput
# user = float(input("Enter your number: "))

# place a condition that checks if the number entered is an even number
# if user % 2 == 0:
#     print(user, 'is an even number.')
# print('am going to be displayed whether you test is right or wrong')

# else condition
# if (user % 2) == 0:
#     print(user, 'is an even number.')
# else:
#     print(user, 'is not an even number.')
# print('this will still print.')

# elif condition

# condition to check if the user entry is even
# if(user / 2 == 2):
#     print(user, 'is an even number.')
#
# # checks if the user entry is odd
# elif(user / 2 ==3):
#     print(user, 'is not an even number.')
#
# # if the user entry is either even or odd
# else:
#     print('Not an even and odd number.')

# while loop
# write a program that prints number 1 to 20

# the nth number
# number = 1
# while(number < 1001):
#     print('\n', number)
#     number += 1
#

# for loop
# creating a list of numbers
# number = [1, 2, -3, 4, -4, 108, 20]
# for index in (number):
#     print('\n', index)

# # looping through the numbers
# # for index in (number):
# # #     if (index > 0):
# # #         continue
# # #     print('\n', index)


# for index in (number):
#     if (index < 0):
#         break
#     print('\n', index)

# write a program that checks if a number is a prime number
# user = int(input('Enter your number: '))
#
# if (user>1):
#     for x in range(2, user):
#         if (user % x == 0):
#             print(user, 'is not a prime number.')
#             break
#     else:
#         print(user, 'is a prime number.')
# else:
#     print(user, 'is not a prime number.')


# user = int(input('Enter your number: '))
#
# if (user > 1):
#     for index in range(2, user):
#         if (user % index == 0):
#             print(user, 'is not a prime number.')
#             break
#     else:
#         print(user, 'is a prime number.')
#
# else:
#     print(user, 'is not a prime number.')


# A program that checks for a leap year
# user = int(input('enter the year: '))
#
# if (user % 4 == 0):
#     if (user % 100 == 0):
#         if (user % 400 == 0):
#             print(user, 'is a leap year.')
#         else:
#             print(user, 'is not a leap year.')
#     else:
#         print(user, 'is a leap year.')
# else:
#     print(user, 'is not a leap year.')

# getting the range of numbers from 1 to 500
# loop through the range of values
# for i in range(1, 501):
#     # checks for values greater than 1
#     if i > 1:
#         # loop through 2 to the 500
#         for m in range(2, i):
#             # checks for non prime numbers
#             if (i % m) == 0:
#                 break
#         else:
#             # print all the possible prime numbers
#             print(i)


# write a program that prints the highest value from the list [2,8,0,6,16,14,1]

# list of numbers
n = [2,8,0,6,16,14,1]

# conditions that checks the size of items in the list.
if n[0] > n[1] and n[2] < n[0] and n[3] < n[0] and n[4] < n[0] and n[5] < n[0] and n[6] < n[0]:
    print(n[0], 'is the highest number')
elif n[1] > n[0] and n[2] < n[1] and n[3] < n[1] and n[4] < n[1] and n[4] < n[1] and n[6] < n[1]:
    print(n[1], 'is the highest number')
elif n[2] > n[0] and n[1] < n[2] and n[3] < n[2] and n[4] < n[2] and n[5] < n[2] and n[6] < n[2]:
    print(n[2], 'is the highest number')
elif n[3] > n[0] and n[1] < n[3] and n[2] < n[3] and n[4] < n[3] and n[5] < n[3] and n[6] < n[3]:
    print(n[3], 'is the highest number')
elif n[4] > n[0] and n[1] < n[4] and n[2] < n[4] and n[3] < n[4] and n[5] < n[4] and n[6] < n[4]:
    print(n[4], 'is the highest number')
elif n[5] > n[0] and n[1] < n[5] and n[2] < n[5] and n[3] < n[5] and n[4] < n[5] and n[6] < n[5]:
    print(n[5], 'is the highest number')
else:
    print(n[6], 'is the highest number')

# # using a default python method
# print(max(n))
















