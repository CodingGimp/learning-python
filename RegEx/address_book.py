import re

names_file = open('names.txt', encoding='utf-8')
data = names_file.read()
names_file.close()

# print(re.match(r'Love', data))
# print(re.search(r'Kenneth', data))
# print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
# print(re.findall(r'\w*' '\w+', data))
print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# print(re.findall(r'\b[trehous]{9}\b', data, re.I))

''' 

def find_words(count, string):
     return re.findall(r'\w{'+ str(count) + ',}', string)

print(find_words(4, "dog, cat, baby, balloon, me"))









New terms
\w{3} - matches any three word characters in a row.
\w{,3} - matches 0, 1, 2, or 3 word characters in a row.
\w{3,} - matches 3 or more word characters in a row. There's no upper limit.

\w{3, 5} - matches 3, 4, or 5 word characters in a row.
\w? - matches 0 or 1 word characters.
\w* - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.

\w+ - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.

[abc] - this is a set of the characters 'a', 'b', and 'c'. It'll match any of those characters, in any order, but only once each.

[a-z], [A-Z], or [a-zA-Z] - ranges that'll match any/all letters in the English alphabet in lowercase, uppercase, or both upper and lowercases.

[0-9] - range that'll match any number from 0 to 9. You can change the ends to restrict the set.

.findall(pattern, text, flags) - Finds all non-overlapping occurrences of the pattern in the text.
'''