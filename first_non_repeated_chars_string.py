def first_non_repeated(string):
    for char in string:
        if string.count(char) == 1: return char 
    #fns return None by default in python, no final return needed for non-match