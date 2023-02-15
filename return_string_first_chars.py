# split string into array
# grab first char of each element
# join back into string

#verbose
def make_string(string):
    words = string.split()
    letters = []
    for word in words:
        letters.append(word[0])
    
    return "".join(letters)


# if you wanna get fancy and use something like a list comprehension
def make_string(string):
    return ''.join([word[0] for word in string.split()])
    # also works without surrounding brackets because join takes any iterable, not just lists