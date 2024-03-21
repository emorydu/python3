def greet(name):
    print(f"Hi {name}")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Emory")
print(message)
file = open("content.txt", "w")
file.write(message)

print(greet("Emory"))   # None


