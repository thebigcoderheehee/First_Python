import random

# print(random.randint(1,9))

# print(random.choice([3, 5, 2, 1, 4, 7, 8, 9, 6]))
# print(random.choice(["!", "@", "$", "%", "^", "&", "*"]))
# print(random.choice(["hello", "harrison", "gentry", "point"]))

# import time

# print("Get Ready In Ten Seconds!")
# time.sleep(10)
# print("Let's Go")

# try:
#     x = 10 / 0
# except:
#     print("Oops! Cannot Divide By Zero")

# print(random.randint(1, 6))
# print(random.randint(1, 6))
# die1 = random.randint(1, 6)
# die2 = random.randint(1, 6)
# total = die1 + die2
# print(f"Your rolls added are {total}")

# print(random.choice(["sticker", "badges", "keychain", "unique coin"]))


try:
    num = int(input("Enter a number!"))
    print(10 / num)
except:
    print("Oops! You can't divide by 0!")