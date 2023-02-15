#fairly easy

#verbose
def reverse_words(words):
    words_arr = words.split(" ")
    reversed_words = words_arr[::-1]
    return " ".join(reversed_words)

# one-liner
def reverse_words(words):
   return " ".join(words.split(" ")[::-1])

# slice is a nice, clean syntax for reversing lists and strings
# non-destructive

# could also do reverse(), but 1) it's destructive, and 2) returns None
# could use reversed, which is nondestructive. returns an iterator object, which you can pass to join