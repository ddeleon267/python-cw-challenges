#fairly simple

def count_positives_sum_negatives(arr):
    if len(arr) == 0: return arr # or some other variation that accounts for empty array

    count_pos = 0
    sum_negs = 0
    for num in arr:
        if num > 0:
            count_pos += 1
        elif num < 0:
            sum_negs += num
    return [count_pos, sum_negs]