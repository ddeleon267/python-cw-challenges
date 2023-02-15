# the codewars directions for this one make my head hurt, but essentially:
# sort list alpabetically
# grab first element from list
# return element as a string, with *** between each letter

#verbose
def two_sort(list):
    sorted_list = sorted(list)
    chosen_word = sorted_list[0]
    return "***".join(chosen_word) 
    # strings are iterables in python, can call join on them directly

# one-liner
def two_sort(list):
    return '***'.join(sorted(list)[0])
    # or can use min() instead of sorted if you wanna get fancy
    #