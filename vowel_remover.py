# only replacing lower-case vowels

# using a loop:
def shortcut(string):
    for vowel in "aeiou":
        string = string.replace(vowel, "")
    return string


# if regex makes your heart sing
import re
def shortcut(string):
    # [] in regex is essentially 'any character in this range'
    new_string = re.sub('[aeiou]', '', s)
    return new_string