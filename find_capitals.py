
# verbose
def capital(capitals): 
    new_list = []
    for dict in capitals:
        state = dict.get('state')
        if state:
            new_list.append(f"The capital of {state} is {dict['capital']}")
        else:
            new_list.append(f"The capital of {dict['country']} is {dict['capital']}")
    
    return new_list

# if a list comprehension speaks to you
def capital(capitals): 
   return [f"The capital of {dict.get('state') or dict['country']} is {dict['capital']}" for dict in capitals]