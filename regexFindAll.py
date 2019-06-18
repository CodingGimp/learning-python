import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

phoneNumRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegex1.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1)

phoneNumRegex2 = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
mo2 = phoneNumRegex2.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo2)











