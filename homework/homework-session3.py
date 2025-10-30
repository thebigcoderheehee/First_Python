testScore1 = int(input("Give Me A Test Score"))
testScore2 = int(input("Give Me Another Test Score"))
testScore3 = int(input("Give Me One Last Test Score"))

print((testScore1 + testScore2 + testScore3) / 3)

num1 = int(input("Give Me A Number"))
num2= int(input("Give Me Another Number"))

if num1 > num2:
    print(f"{num1} is bigger than {num2}")
elif num2 > num1:
    print(f"{num2} is bigger than {num1}")
else:
    print(f"{num1} and {num2} are the same")

pizza_slizes = int(input("How many pizza slices do you have?"))
friends = int(input("How many friends do you have?"))
print("Each of your friends get", pizza_slizes / friends, "pizza" \
"slices")
print("The leftovers are", pizza_slizes % friends, "pizza slices")