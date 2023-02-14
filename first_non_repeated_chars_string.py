def first_non_repeated(s):
    for char in s:
        if s.count(char) == 1: return char 
    #fns return None by default in python, no final return needed