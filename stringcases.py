''' Create a function named stringcases that takes a single string but returns a tuple of different string formats. The formats should be:

All uppercase
All lowercase
Titlecased (first letter of each word is capitalized)
Reversed
There are str methods for all but the last one.

'''

def stringcases(string):
    uppercase = string.upper()
    lowercase = string.lower()
    titlecase = string.title()
    reverse = string[::-1]

    tup = uppercase, lowercase, titlecase, reverse

    return tup

stringcases('i love you')