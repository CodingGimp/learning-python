import re

beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello world!')
mo1 = beginsWithHello.search('He said "Hello world!"')
print(mo.group())

