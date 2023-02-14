# a bit challenging!
# remember that sorted() always returns a list/array!


# my initial solution:
# if you want to use a list comprehension instead
def convert_hash_to_array(dict):
    return [[key, val] for key, val in sorted(dict.items())]

# verbose, if that's helpful for your student
def convert_hash_to_array(dict):
    sorted_list = sorted(dict.items()) # sorting by key, get back list of tuples formatted like (key, val)
    new_array = []
    for key, val in sorted_list:
        new_array.append([key, val])
    return new_array




############################# OTHER SOLUTIONS - find one that clicks for you! ######################    
def convert_hash_to_array(dict): 
    return [[key, dict[key]] for key in sorted(dict)]
    # this is similar to my solution, but when you call sorted on dict you just get a list of the keys
    # so need to refer back to original dict for values


def convert_hash_to_array(dict):
    return sorted(list(item) for item in dict.items())
    # list returns a list, so does the same as [] in the list comprehension


def convert_hash_to_array(dict): 
    return sorted(map(list, dict.items()))
    # map follows the format map(function_to_apply, iterable)
    


