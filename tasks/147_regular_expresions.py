'''
? matches pattern optionally
* matches 0 or more times
+ matches 1 or more times
{n,m} matches specified amount of repetition
{n,m}? or *? or +? performs a nongreedy match of the preceding group.
^ - match must happen at the beginning of the text
$ - match must happen at the end of the text
\d digits
\D non digits (any character that is not number 0 to 9)
\w letters, digits, underscore character '_'
\W anything that is not letter, digit, _
\s any space, tab, newline character \n
\S opposite of the above
. - matches anything except newline
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets.
'''

import re

message1 = "You can contact me calling to my number: 430-444-2939."

def findNumber(text): #\d finds a number in a text
    phoneNumRex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    pf = phoneNumRex.search(text)
    print('Phone numbers found: ' + pf.group())

    #will find all number slices with 1 or 2 digits
    checking1 = re.compile(r'\d{1,2}')
    checking2 = checking1.findall(text)
    print(checking2)

def subString(text):
    subRegex = re.compile(r'\d\d\d+')
    sub1 = subRegex.sub('***', text)
    print(sub1)

def ignoreCase(text):
    iC = re.compile(r'you', re.IGNORECASE | re.DOTALL | re.VERBOSE)
    iC2 = iC.search(text)
    print(iC2.group())

findNumber(message1)
subString(message1)
ignoreCase(message1)