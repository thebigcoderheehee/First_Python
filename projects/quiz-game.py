questions = {"2 + 3?": "5", "Capital of India?": "Delhi", "Color of grass?": "Green"}

score = 0

for q, a in questions.items():
    answer = input(q)
    if answer.lower() == a.lower():
        print("You got it right!")
        score += 1

if score == 0:
    print("YOU GOT NONE RIGHT!!! GET SOME HELP!")
elif score == 1:
    print("You got 1 right! You only need a little bit of help!")
elif score == 2:
    print("If you don't get it the first time, try, try again!")
else:
    print("YOU GOT THEM ALL RIGHT!!! YOU RULE!")