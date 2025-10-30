age = int(input("What is your age!"))

if age > 8:
    print("Your old enough!")
elif age < 8:
    print("You're too young!")
else:
    print("You're in the middle!")

num1 = int(input("Give me a number!"))
num2 = int(input("Give me another number!"))

if num1 == num2:
    print("Yay!")
else:
    print("Nooooo!")

room_clean = input("Is your room clean?")
homework_done = input("Is your homework done?")

if homework_done == "yes" and room_clean == "yes":
    print("Hurray!")
elif homework_done == "no" and room_clean == "no":
    print("Oh No!")
elif homework_done == "yes" and room_clean == "no":
    print("Oh No!")
else:
    print("Oh No!")