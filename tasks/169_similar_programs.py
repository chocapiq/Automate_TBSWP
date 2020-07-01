import pyperclip, re

#finds the base URLs in copied text
def findURL(text):
    URLRegex = re.compile(r'''(
    http(s)?\:// #protocol, we are looking for only http/https
    (www\.)? #start with www, optional
    [a-zA-Z0-9_+?=#]+ #server adress
    \.[a-z]{2,5} #domain
    )''', re.VERBOSE)
    extractedURL = URLRegex.findall(text)
    allURL = []
    for url in extractedURL:
        allURL.append(url[0])
    urlResults = '\n'.join(allURL) + '\n'
    print("Found URLs: \n" + urlResults)
    return urlResults

#finds and standarizes date format to dd/mm/yyyy
def findAndSubDate(text):
    dateRegex = re.compile(r'''(
    (\d{1,4}) # find first numbers of the date
    (\s|-|\.|/){1} #separator for date
    (\d{1,2}) #finds middle numbers of the date, it might be day or month
    (\s|-|\.|/){1} #separator for date
    (\d{1,4})
    )''', re.VERBOSE)
    extractedDate = dateRegex.finditer(text)
    allDates = []
    for i in extractedDate: #filters data-like text that has 3 numbers since i.e. 333/10/11 won't be a date, middle text is either month or day so it's number in range 1 to 31
        if len(str(i.group(2))) != 3:
            if len(str(i.group(6))) != 3:
                if int(i.group(4)) in range (1,32):
                    allDates.append(i.group(1))
    allDatesSub = []
    subbingRegex1 = re.compile(r''' # changes diffrent separators to /
    (\s|-|\.|/){1}
    ''', re.VERBOSE)
    for j in allDates:
        allDatesSub.append(subbingRegex1.sub('/', j))
    dateResults = '\n'.join(allDatesSub) + '\n'
    print("Found dates: \n" + dateResults)
    return dateResults

def commonTextErrors(text):
    subRegex1 = re.compile(r'''
    \s{2,} #finds double spaces
    ''', re.VERBOSE)
    subRegex2 = re.compile(r'''(
    [!]{2,} #finds double exclamation marks
    )''', re.VERBOSE)
    subRegex3 = re.compile(r'''
    \b # finds words
    (\w+) #searches for words
    \s+ #space
    \1 #finds if the group 1 is a repetition
    \b
    ''', re.VERBOSE)
    doubleWords = subRegex3.findall(text)
    text1 = subRegex1.sub(' ', text)
    text2 = subRegex2.sub('!', text1)
    text3 = subRegex3.sub('gg', text2) #workaround to replace double words with temporary word and swap it later by iterating through list
    for i in doubleWords:
        text3 = text3.replace('gg', i, 1)
    print(text3)
    return text3

findInText = str(pyperclip.paste())
#findURL(findInText)
#findAndSubDate(findInText)
#commonTextErrors(findInText)