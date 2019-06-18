import re

batRegex = re.compile(r'Bat(wo)?man') #The regex will match text that has zero instances or one instance of wo in it. 

mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('Call me at 426-8442')
print(mo.group())

bat2Regex = re.compile(r'Bat(wo)*man')
mo1 = bat2Regex.search('The Adventures of Batman')
mo2 = bat2Regex.search('The Adventures of Batwoman')
mo3 = bat2Regex.search('The Adventures of Batwowowowoman')

print(mo1.group())
print(mo2.group())
print(mo3.group())


bat3Regex = re.compile(r'Bat(wo)+man')
mo4 = bat3Regex.search('Batman and Robin')
mo5 = bat3Regex.search('Batwoman and Batgirl')
mo6 = bat3Regex.search('Batwowowoman and Batgirl')

print(mo4 == None)
print(mo5.group())
print(mo6.group())




haRegex = re.compile(r'(Ha){3}')
mo7 = haRegex.search('He said "HaHaHa"')
print(mo7.group())

haRegex1 = re.compile(r'(Ha){3,5}')
mo8 = haRegex1.search('He said "HaHaHaHaHaHa"')
print(mo8.group())

