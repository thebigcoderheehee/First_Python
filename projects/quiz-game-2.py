questions = { "5+5?": "10", "Sun rises from?": "East", "Python is a?": "Language", "3*4?": "12", "Color of sky?": "Blue"}

score = 0

for q, a in questions.items():
    answer = input(q + " ")
    if answer.lower() == a.lower():
        score += 1

print(f"Your score is: {score}!")

if score >= 4:
    print("Brilliant!")
else:
    print("Try again!")