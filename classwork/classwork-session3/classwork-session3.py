candies = int(input("How many candies do you have?"))
friends = int(input("How many friends do you have?"))
print("Each of your friends get", candies / friends, "candies")
print("The leftovers are", candies % friends, "candies")