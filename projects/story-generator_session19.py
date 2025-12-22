import random

twists = ["found treasure", "met a dragon", "got lost", "found magic sword"]

hero_name = input("Give me a name of a hero!")
place_name = input("Give me a name of a place!")
villain_name = input("Give me a name of a villian!")

print(hero_name, "went to", place_name, random.choice(twists), "but the villain", villain_name, "appeared!")