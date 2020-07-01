#finds specified text from clipboard, here it finds NA phone numbers and emails
import pyperclip, re

#finding phone number
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? #area code, 3 first numbers
(\s|-|\.)? #separator
(\d{3}) #first 3 digits after area code
(\s|-|\.)? #separator
(\d{4}) #last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? #extension with optional numbers
)''', re.VERBOSE)

#finding email
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ #username
@
[a-zA-Z0-9.-]+ #domain
(\.[a-zA-Z]{2,4}) # finishing domain after dot
)''', re.VERBOSE)

#find matches from clipboard text
text = str(pyperclip.paste())

#extract email and phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
allEmailAdresses = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
for emailAdress in extractedEmail:
    allEmailAdresses.append(emailAdress[0])
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(allEmailAdresses)
pyperclip.copy(results)




