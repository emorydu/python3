letters = ["a", "b", "c"]

# Add
letters.append("d")
letters.insert(0, "-")
print(letters)

# Remove
letters.pop()
letters.pop(0)
letters.remove("b")
del letters[0:2]
letters.clear()

del letters
print(letters)

