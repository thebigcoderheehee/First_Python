num1 = int(input("Choose a number"))
num2 = int(input("Choose a second number"))
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)
if operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 != 0:
        print(num1 / num2)
    print("Undefined")
else:
    print("Invalid operation! Please choose +, -, * or /.")