# Write a progrma that checks if the year entered by the user is a LEAP YEAR OR NOT.

# First we understand what a leap year is.
# A leap year is exactly divisible by 4 except for century years (i.e any year that ends with double zeros (00))
# The century year is a leap year if it is perfectly divisible by 400.

#functions
def leap():
    print("is a Leap Year.")

def not_leap():
    print("is not a Leap Year.")
    
def leap_year(entry):
    if (int(entry) % 4) == 0:
        if (int(entry) % 400) == 0:
            leap()
        else:
            not_leap()
    else:
        not_leap()



# main program
userinput = input("\nEnter any of your choice: ")
if int(len(userinput)) <4 or not(int(len(userinput)) <4): # the 'not' keyword negate any condition that comes after it.
    print("your input is either lower than 4 digits or higher than 4 digits.")
else:
    leap_year(int(userinput))

print("Thanks for playing.")
    

        
                        