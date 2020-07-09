import time
import pyperclip

timestr = time.strftime("%Y%m%d-%H%M%S")

MadLibsBase = open('.\\mad libs text\\MadLibsBase.txt', 'r').read()
MadLibs = open('.\\mad libs text\\MadLibsBase_%s.txt' % (timestr), 'w')

pyperclip.copy(MadLibsBase)
text = str(pyperclip.paste())

ADJECTIVE1_input = input(str('Enter an adjective:\n'))
NOUN1_input = input(str('Enter a noun:\n'))
VERB1_input = input(str('Enter a verb:\n'))
NOUN2_input = input(str('Enter a noun:\n'))

text = text.replace('ADJECTIVE', ADJECTIVE1_input)
text1 = text.replace('NOUN', NOUN1_input, 1)
text1 = text1.replace('VERB', VERB1_input)
text1 = text1.replace('NOUN', NOUN2_input, 1)

MadLibs.write(text1)