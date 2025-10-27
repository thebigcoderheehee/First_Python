password = 7
guess = 0

while guess != password:
    guess = int(input("Guess a number: "))
print("Great job!!!")

timer = 10

while timer >= 1:
    print(timer)
    timer -= 1
print("BLASTOFF!!!")

color = "blue"
guess = "0"

while guess.lower() != color:
    guess = input("Guess a color: ")
print("Great job!!!")

timer = 100

while timer >= 50:
    print(timer)
    timer -= 1
print("BLASTOFF!!!")

name = "Fateh"
name = name.lower()
guess = "0"

while guess.lower() != name:
    guess = input("Guess a name: ")
print("Great job!!!")