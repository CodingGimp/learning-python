'''
Create a function named find_emails that takes a string. Return a list of all of the email addresses in the string.
'''
import re
def find_emails(s):
    return re.findall(r'[-\w\d+.]+@[-\w\d.]+', s)

print(find_emails("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk"))