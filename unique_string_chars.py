# if you just want to deal with strings
def solve(first_str, second_str):
    uniq_chars = ""
    for char in first_str:
        if char not in second_str: 
            uniq_chars += char
        
    for char in second_str:
        if char not in first_str: 
            uniq_chars += char
        
    return uniq_chars

# if you wanna use lists / list comprehensions
def solve(first_str, second_str):
    # loop over first_str
    first_search_chars = [char for char in first_str if not char in second_str]
    # loop over second str
    second_search_chars = [char for char in second_str if not char in first_str]
    # combine lists and join back together
    return "".join(first_search_chars + second_search_chars)


# if you don't wanna loop over every char in both strings, you'll need to use sets
    # sets: https://www.w3schools.com/python/python_sets.asp
    # intersection: https://www.w3schools.com/python/ref_set_intersection.asp
def solve(first_str, second_str):
    uniq_chars = ""
    # Return a set that contains the items that exist in both sets:
    common_char_set = set(first_str).intersection(set(second_str)) 

    for char in first_str + second_str:
        if char not in common_char_set:
            uniq_chars += char
    
    return uniq_chars
    # can clean up with list comprehension + join if you like
    
