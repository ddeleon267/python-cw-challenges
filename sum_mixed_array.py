#fairly simple

def sum_mix(arr):
    my_sum = 0
    for maybe_num in arr:
        my_sum += int(maybe_num)
    return my_sum

# if you wanna get fancy and use built-ins
def sum_mix(arr):
    return sum(map(int,arr))
    #map -> takes args of a function and an iterable, returns an iterable