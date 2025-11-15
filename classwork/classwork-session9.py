games = ["chess", "cricket", "ludo"]
#           0         1         2
print(games)
games.append("football")
print(games)
# games.remove("ludo")
print(games)
print("I love to play")
for game in games:
    print("I love to play", game)
print("Total Games:", len(games))
print(games[-1])

required_items = ["rope", "map", "compass", "boots", "rainjacket", "tent", "matches", "toiletries"]
print("I have:", required_items)
required_items.append("lunch")
print("I have added;", required_items)
required_items.remove("tent")
print("I have removed;", required_items)
print("Total Items:", len(required_items))

