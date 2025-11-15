dictionary1 = {"name":"Fateh"}

scores = {"Fateh":21, "Zara":10}

print(scores, "out of 20")

# print(len(scores))

# print(scores["Fateh"], "out of 20")

# scores["Zara"] += 5
# print(scores, "out of 20")

# for name, score in scores.items():
#     print(name, "scored", score)

# friends = {"Alexander":11, "Arturo":12, "Harrison":13}

# oldest = max(friends, key = friends.get)
# youngest = min(friends, key = friends.get)

# print("My oldest friend is", oldest)
# print("My youngest friend is", youngest)

# fruits = {"Apple":50, "Banana":25, "Grapefruit":500, "Mango":58, "Grapes":35463}
# print(fruits["Apple"] + fruits["Banana"] + fruits["Mango"])
# totalABM = fruits["Apple"] + fruits["Banana"] + fruits["Mango"]
# print(totalABM)
# print(totalABM + fruits["Banana"])

books = {"math":"borrowed", "algebra":"available", "history":"available", "geography":"borrowed"}

for name, availability in books.items():
    print(name, "is", availability)

print(books["algebra"])
books["math"] = "available"
print(books)

for availability in books.values():
    print(availability)

books["biology"] = "borrowed"
print(books)
books.pop("geography")
print(books)
books.popitem()
print(books)
print("algebra" in books)
print(len(books))

books2 = books.copy()
print("Books", books)
print("Books2", books2)
books2.pop("math")
print("Books2 without math:", books2)
books2["algebra"] = "borrowed"
print("Books2 with borrowed algebra:", books2)
books.update(books2)
print("Books", books)
print("Books2", books2)
books.clear()
print("Books", books)