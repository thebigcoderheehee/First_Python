#
# snack1 = "chips"#
# snack2 = "cookies"#
# print(snack1, snack2)# tem = snack1# snack1 = snack2# snack2 = tem# print(snack1, snack2)

# favcolor = input("What is your favorite color?")# favanimal = input("What is your favorite animal?")# favsport = input("What is your favorite sport?")# print("You like", favcolor, favanimal + "'s", "who play", favsport)# print("You like", favcolor.upper(), favanimal.upper() + "'s", "who play", favsport.upper())# print((f "You like {favcolor} {favanimal}'s who play {favsport}").upper())

# coinsfound1 = int(input("How many coins did you find?"))# coinsfound2 = int(input("How many coins did you find?"))# coinsfound3 = int(input("How many coins did you find?"))

# totalcoins = 0# totalcoins = coinsfound1 + coinsfound2 + coinsfound3


# print("You found", totalcoins, "coins! Great job!")

# kids = int(input("How many kids are there?"))# pizza_slices = int(input("How many pizza slices are there?"))

# slices_per_kid = 0# slices_per_kid = pizza_slices // kids

# leftovers = pizza_slices % kids


# print(f "If you divide pizza slices by kids, you will get the number of slices each kid gets, which is {slices_per_kid}. The leftovers are {leftovers} pizza slices.")

# base = int(input("Enter a number you want to grow bigger: "))
# exponent = int(input("Enter how many times you want to multiply it by itself: "))

# result = base ** exponent


# print(f"Your final, grown number is {result}")

# scores = []

# for i in range(5):
#     score = int(input("Give me a score."))
#     i = i + 1
#     scores.append(score)

# average = sum(scores) / 5
# print(f"Your average score is {average}")



# kids = int(input("How many kids are there?"))# pizza_slices = int(input("How many pizza slices are there?"))

# slices_per_kid = 0# slices_per_kid = pizza_slices // kids

# leftovers = pizza_slices % kids


# print(f "If you divide pizza slices by kids, you will get the number of slices each kid gets, which is {slices_per_kid}. The leftovers are {leftovers} pizza slices.")

# money = int(input("How much money do you have?"))
# price = int(input("What is the price of your toy?"))

# things_you_can_afford = money // price

# extra_money = money % price

# print(f"You can buy {things_you_can_afford} toys and are remained with ${extra_money}")


# age = int(input("How old are you?"))
# height = int(input("How tall are you?"))

# answer = (age >= 8 and height >= 120)
# print(answer)

# if age >= 8 and height >= 120:
#     print("Yes")
# elif age <= 8 and height >= 120:
#     print("No")
# elif age >= 8 and height <= 120:
#     print("No")
# else:
#     print("No")


# if height >= 120 and age >= 8:
#     print("Yes, you can ride")
# else:
#     print("No, you cannot ride")


# homework = input("Is your homework done?")
# room = input("Is your room clean?")

# if room == "yes" and homework == "yes":
#     print("You can have cake!")
# else:
#     print("You can't have cake.")



# secretword1 = "open"
# secretword2 = "sesame"

# userword = input("Give me a word to open a door.")

# if userword == secretword1 or userword == secretword2:
#     print("*DOOR OPENING*")
# else:
#     print("WRONG PASSWORD")

# weather = input("Is is raining?")

# is_dry = not(weather == "yes")


# print(is_dry)


# result = int(input("Give me a score!"))

# if result > 90 or result == 90:
#     print("You got an A!")

# elif result > 80 or result == 80:
#     print("You got an B!")

# elif result > 70 or result == 70:
#     print("You got an C!")

# elif result > 60 or result == 60:
#     print("You got an D!")

# else:
#     print("You got an F!")


# for i in range(1, 30):
#     if i % 2 != 0:
#         print(i)

# for i in range(1, 30):
#     if i % 2 == 0:
#         print(i)

# for i in range(1, 6):
#     print("*" * i)


# for i in range(20, -1, -2):
#     print(i)

# name = "fateh"


# for i in name:
#     print(f"[{i}]".upper())

# while True:
#     name = input("Enter a name!")

#     if name == "fateh":
#         print("YOU GUESSED IT!!! OH MY GOD!!! GOOD JOB!!!")
#     else:
#         print("Try again. You'll get it. Someday.")


# while True:
#     secretnumber = int(input("Enter a number!"))

#     if secretnumber == 5:
#         print("YOU GUESSED IT!!! OH MY GOD!!! GOOD JOB!!!")
#         break
#     else:
#         print("Try again. You'll get it. Someday.")

# actualpassword = "fateh11"
# attempts = 0
# while attempts < 3:
#     password = input("Guess A Password!")

#     if password == actualpassword:
#         print("Unlocked!")
#         break
#     else:
#         attempts += 1
#         if attempts <= 2:
#             print("Try Again!")
#         else:
#             print("Locked! Security Alert!")


# number = 0
# while True:
#     usernumber = int(input("Give me a number"))

#     if usernumber == 0:
#         print(number)
#         break
#     else:
#         print("Keep Going!")
#         number += usernumber

# if number = 12, 14, 16, then continue
# if number = 19 or 21, then break

# for i in range(2, 25):
#     if i == 12:
#         continue
#     if i == 19:
#         break
#     print(i)


# def sayhello(n):
#     for i in range(n):
#         print("Hello")
# n = int(input("Give me a number."))
# sayhello(n)


# a = int(input("Give me a number"))
# b = int(input("Give me another number"))
# c = int(input("Give me a third number"))
# def biggest(a, b, c):
#     if a >= b and a >= c:
#         print(a)
#     elif b >= a and b >= c:
#         print(b)
#     else:
#         print(c)
# biggest(a, b, c)


# def is_prime(n):
#     if n < 2:
#         return "It is not prime!"
#     for i in range(2, n):
#         if n % i == 0:
#             return "It is not prime!"
#     return "It is prime!"

# n = int(input("Give me a number"))
# print(is_prime(n))


# user_password = input("Give me a password")
# def check_password(user_password):
#     if len(user_password) >= 8:
#         return "Strong Password"
#     else:
#         return "Weak Password"
# print(check_password(user_password))

# check_password(user_password)


# numbers = []
# for i in range(5):
#     num = int(input("Enter a number!"))
#     numbers.append(num)
# print(numbers)
# print("The biggest number is:", max(numbers))
# print("The smallest number is:", min(numbers))
# print("The sum of all your numbers is:", sum(numbers))

# words = ["apple", "banana", "cat", "dog"]
# print(words)
# reversed_word = []
# for word in reversed(words):
#     reversed_word.append(word)
# print("Your words backwards are:", reversed_word)