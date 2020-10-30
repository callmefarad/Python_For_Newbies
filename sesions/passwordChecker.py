# a program that checks if a password is too weak, weak and very strong
# defining the function
def copywrite():
    print("Copywrite: Ubani U. Friday")

# main function
special_characters = ['!', '^', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+']
special_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
upper_character = ['A','B','C','D','E','F','G','H','I','J','K','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

counter_character = 0
counter_number = 0
counter_upper = 0
list_holder = []

userinput = input("Enter your password: ")
list_holder = list_holder + list(userinput)
for i in range(len(userinput)):
    if list_holder[i] in special_characters:
        counter_character += 1
    if list_holder[i] in special_numbers:
        counter_number += 1
    if list_holder[i] in upper_character:
        counter_upper += 1
if len(userinput)<7:
    print("TOO WEAK, please include numbers and special characters")
elif len(userinput)>=7 and counter_number>0 and counter_character>0 and counter_upper >0:
    print("VERY STRONG password.")
else:
    print("The password is WEAK")
copywrite()


