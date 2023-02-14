#fairly simple

def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'

#or, if you wanna loop
def find_needle(haystack):
    for i, str in enumerate(haystack):
        if str == "needle":
            return f"found the needle at position {i}"