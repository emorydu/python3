point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point["x"])
print(len(point))

if "a" in point:
    print(point["a"])

print(point.get("a"))   # None
print(point.get("a", 0))
del point["x"]
print(point)

for key in point:
    print(key, point[key])

for k, v in point.items():
    print(k, v)


# list()
# tuple()
# set()
# dict()
