# if you wanna build out sum logic
def summation(num):
    sum = 0
    for current_num in range(num+1):
        sum += current_num
    return sum

# if you wanna use the built-in fn
def summation(num):
    return sum(range(1,num+1))
    #