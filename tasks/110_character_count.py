import pprint
import re

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

#def will count characters if value is 0, else it will count how many times words appear in a text
def countingWordsAndCharacters(text, characters=0):
    count = {}
    if characters == 0:
        for character in text.lower():
            count.setdefault(character, 0)
            count[character] += 1
    else:
        wordList = re.sub("[^\w]", " ",  text.lower()).split()
        for character in wordList:
            count.setdefault(character, 0)
            count[character] += 1

    #r = pprint.pformat(count)
    #print(r)
    pprint.pprint(count)
countingWordsAndCharacters(message, 1)