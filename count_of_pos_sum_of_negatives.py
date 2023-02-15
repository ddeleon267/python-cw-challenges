def count_positives_sum_negatives(list):
    if len(list) == 0: return list # or some other variation that accounts for empty list

    count_pos = 0
    sum_negs = 0
    for num in list:
        if num > 0:
            count_pos += 1
        elif num < 0:
            sum_negs += num
    return [count_pos, sum_negs]