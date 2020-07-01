import re
password = input('Type password to validate its strength.')

passRegex1 = re.compile(r'[A-Z]+') #checks string for at least one uppercase
passRegex2 = re.compile(r'[a-z]+') #checks string for at least one lowercase
passRegex3 = re.compile(r'[0-9]+') #checks string for at least one number

upperPass = passRegex1.search(password)
lowerPass = passRegex2.search(password)
numPass = passRegex3.search(password)
x = 0
if upperPass != None:
    x += 1
if lowerPass != None:
    x += 1
if numPass != None:
    x += 1
if len(password) >= 8:
    x += 1
print(x)
if x <= 2:
    print("Password is weak.")
if x == 3:
    print("Medium strength password.")
if x == 4:
    print("Password is strong.")