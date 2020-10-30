# This is a basic calcultor that performs four operations (addition, subtraction, multiplication and divition)

print("\nThe operations are this calculation are +, -, * and /")
num1 = float(input("Enter your first number: "))
op = input("Enter your operator: ")
num2 = float(input("Enter your second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
else:
    print("INVALID OPERATOR")



