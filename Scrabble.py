# A scrabble game hacker V2
from time import time
start = time()
# Checks if a word S1 is made out of a set of letters S2
def string_contains_string(s1):
    s1 = s1.upper()
    s2 = list(letters.upper())
    for o in s1:
        if o in s2:
            s2.remove(o)
        else:
            return False
    return True


# Imports words from a dictionary
with open('dictionary.txt', 'r') as fobj:
    words = fobj.read().split()

# Letters to search for
letters = input("Enter letters:")
possibilities = filter(lambda x: len(x) <= len(letters), words)
output = list(filter(lambda x: string_contains_string(x), possibilities))
print(output)
print(start - time())
