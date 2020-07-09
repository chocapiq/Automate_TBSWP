import re, os

'''path = '.\\mad libs text'''
#asks for path
path = input('Enter folder name you want to search inside\n')
#creates absolute path
absPath = os.path.abspath(path)
#what word you want to look for in a text file
textToFind = input('What do you want to find in a text?\n')
#changes working directory, otherwise won't find text file with 'open' function
os.chdir(absPath)
#loops through files in a directory trying to find input word, prints result as how many specified words were find in a file
for txtfile in os.listdir(absPath):
    n = 0
    if txtfile.endswith('.txt'):
        textRead = open(txtfile).read()
        textRegex = re.compile(textToFind)
        wordsFound = textRegex.findall(textRead)
        for wordFound in wordsFound:
            n += 1
        print('Found ' + str(n) + ' ' + str(textToFind) + ' inside file ' + str(txtfile))

