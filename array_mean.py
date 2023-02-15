def find_average(nums):
    # tests try an empty list so need to account for division by 0
    length = len(nums)
    return sum(nums) / length if length > 0 else 0
    
    
    # or if you don't wanna use sum, ternary
    # if length > 0:
    #     sum = 0
    #     for num in nums:
    #         sum += num
    #     return sum / len(nums)
    # else:
    #     return 0