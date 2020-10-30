# Calculator app
import moduletest


print("Welcome: Calculator app is free for use.")
# print("Do you wish to carry out another operation?", end='\n')
# print("Press 8: to start again.", end='\n')
# print("Press 0: to exit the program.", end='\n')
# userdefault = input()
# while (userdefault == 8):
user = input('Enter your name: ')
if (len(user) == 0):
    print("Name of user can't be empty")
else:
    print("Welcome: ", user.capitalize())
    print('Press 1: for addition operation', end="\n")
    print('Press 2: for subtraction operation', end="\n")
    print('Press 3: for multiplication operation', end="\n")
    print('Press 4: for division operation', end="\n")
    print('Press 5: to exit the program', end="\n")

    userinput = int(input('What operation do you want to perform? '))
    if (userinput == 1):
        # addition operation
        firstNumber = float(input('Enter your firstnumber: '))
        secondNumber = float(input('Enter your secondnumber: '))
        print(moduletest.add(firstNumber, secondNumber))

    elif (userinput == 2):
        # subtraction
        firstNumber = float(input('Enter your firstnumber: '))
        secondNumber = float(input('Enter your secondnumber: '))
        print(moduletest.sub(firstNumber, secondNumber))

    elif (userinput == 3):
        # multiplication
        firstNumber = float(input('Enter your firstnumber: '))
        secondNumber = float(input('Enter your secondnumber: '))
        print(moduletest.mult(firstNumber, secondNumber))

    elif (userinput == 4):
        # division
        firstNumber = float(input('Enter your firstnumber: '))
        secondNumber = float(input('Enter your secondnumber: '))
        print(moduletest.div(firstNumber, secondNumber))
    else:
        print('Program exited....')
