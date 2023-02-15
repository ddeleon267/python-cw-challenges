#fairly simple

# if you wanna loop
def sum_mix(arr):
    my_sum = 0
    for maybe_num in arr:
        my_sum += int(maybe_num) 
        # could check if it's an int already but not sure it makes much of a difference performance-wise
    return my_sum

# if you wanna get fancy and use built-ins
def sum_mix(arr):
    return sum(map(int,arr))
    #map -> takes args of a function and an iterable, returns an iterable