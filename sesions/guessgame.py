# write a number guess game where the user has three chances of getting the answer
# correctly.

#importing the random class so we can use random.choice
import random


#creating reuseable funtions
def copywrite():
    print("Copywrite: Ubani U. Friday")

def footer():
    print("#" * 40)


count = 3
starter = input("Enter 0 to start OR any number > 0 to end the game: ")
if int(starter) == 0:
    while count > 0:
        print('Guess the hidden number between 1 and 5 to win yourself a bottle of coke')
        userinput = int(input("Enter your number: "))
        if (intuserinput == int(random.choice(range(1, 6)))):
            footer()
            print("The hidden number is: ", int(userinput), "You've won yourself a bottle of coke. ")
            footer()
            break
        else:
            print("You Failed Woefully.")
            count -= 1
else:
    print("You entered the wrong number.")

print("\nThanks for playing.")
copywrite()






