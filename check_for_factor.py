# very easy

# clear / simple option
def check_for_factor(base, factor):
    return base % factor == 0

# works because 0 is falsey in python
# 0 result means it's a factor, so you negate the logic
def check_for_factor(base, factor):
    return not (base % factor)