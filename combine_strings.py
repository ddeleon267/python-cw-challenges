# f string seems to be most modern way
def combine_names(first_name, last_name):
    return f"{first_name} {last_name}"

# more old school
def combine_names(first, last):
    return first + " " + last

# super old school
def combine_names(first, second):
    return '{} {}'.format(first, second)