number = int(input("Give me any number!"))

if number >= 50:
    print("Good job! You had a high number!")
else:
    print("Oops, too low.")

num1 = int(input("Give me a number.")) 
num2 = int(input("Give me another number."))

if num1 > num2:
    print("The first number is bigger.")
elif num1 == num2:
    print("Your numbers match.")
else:
    print("You're too low.")

word = "glasses"
user_guess = input("Guess a word.")

if user_guess == word:
    print("You're a mind reader! You guessed the word! Amazing job!")
else:
    print("Try the rest of the dictionary🤣!")
