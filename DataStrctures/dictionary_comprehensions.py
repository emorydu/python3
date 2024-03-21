values = []
for x in range(5):
    values.append(x * 2)

values = [x*2 for x in range(5)]
print(values)


values = {x * 2 for x in range(5)}  # sets
print(values)

values = {}
for x in range(5):
    values[x] = x * 2

print(values)

values = {x: x * 2 for x in range(5)}
print(values)

values = (x * 2 for x in range(5))
print(values)

