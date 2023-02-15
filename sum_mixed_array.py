# if you wanna loop
def sum_mix(list):
    my_sum = 0
    for maybe_num in list:
        my_sum += int(maybe_num) 
        # could check if it's an int already but not sure it makes much of a difference performance-wise
    return my_sum

# if you wanna get fancy and use built-ins
def sum_mix(list):
    return sum(map(int,list))
    #map -> takes args of a function and an iterable, returns an iterable