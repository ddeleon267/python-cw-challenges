# the directions for this one make my head hurt, but essentially:
# sort array alpabetically
# grab first element
# return element with *** between each letter

#verbose
def two_sort(array):
    sorted_arr = sorted(arr)
    chosen_word = sorted_arr[0]
    return "***".join(chosen_word) 
    # strings are iterables in python, can call join on them directly

# one-liner
def two_sort(arr):
    return '***'.join(sorted(arr)[0])
    # or can use min() instead of sorted if you wanna get fancy