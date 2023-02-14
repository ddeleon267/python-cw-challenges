# a littler trickier
# only replacing lower-case vowels


# using a loop:
def shortcut(s):
    for vowel in "aeiou":
        s = s.replace(vowel, "")
    return s


# if regex makes your heart sing

import re
def shortcut(s):
    # [] in regex is essentially 'any character in this range'
    new_s = re.sub('[aeiou]', '', s)
    return new_s