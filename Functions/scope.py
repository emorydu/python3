message = "a"   # global variable (in file)

def greet(name):
    message = "b"


def send_email(name):
    message = "b"


def greet2(name):
    global message
    message = "b"   # modify global variable


greet("Emory")
print(message)  # access global variable
# print(name)

greet2("Emory")
print(message)  # access global variable