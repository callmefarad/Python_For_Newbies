import except_module as em

# the program in proper
# call the function from em
z = True
n = ""
while z:
    try:
            d = input("type e to exit or c to continue.")
            if d == "e":
                z=False
                break
            elif d == "c":
                z=True
            a = int(input("Enter the first number: "))
            C = int(input("Enter the second number: "))
            em.sum(a, C)
    except ValueError as ve:
        print(ve)
    except NameError as ne:
        print(ne)
if a or C == n:
    z = False

