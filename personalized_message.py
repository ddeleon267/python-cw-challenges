# if you wanna go the traditional route:
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

# if you wanna hit 'em with the one-liner:
def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"