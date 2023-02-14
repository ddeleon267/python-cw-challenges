# if you wanna loop

def sum_mul(n, m):
    # n is factor, m is multiple of factor
    if m > 0 and n > 0:
        calc_sum = 0
        for current_num in range(n, m, n):
            calc_sum += current_num
        return calc_sum
    else:
        return "INVALID"

# if you wanna use built-in fn for sum:

def sum_mul(n, m):
    # n is factor, m is multiple of factor
    if m > 0 and n > 0:
        calc_sum = 0
        for current_num in range(n, m, n):
            calc_sum = sum(range(n, m, n))
        return calc_sum
    else:
        return "INVALID"