try:
    with open("app.py") as file, open("another.py") as target:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10 / 0
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
