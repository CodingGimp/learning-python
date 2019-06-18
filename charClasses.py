import re

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

print(mo)

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo2 = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(mo2)

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
mo3 = doubleVowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(mo3)

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo4 = consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
print(mo4)