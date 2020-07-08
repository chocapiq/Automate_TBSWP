#! python3
# Usage:
# py.exe mcb.pyw save <keyword> saves clipboard to keyword
# py.exe mcb.pyw <keyword> loads keyword to clipboard
# py.exe mcb.pyw list - loads all keyword to clipboard
# py.exe mcb.pyw del <keyword> removes keyword from cliboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content. len = 4???
if sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif sys.argv[1].lower() == 'del':
    del mcbShelf[sys.argv[2]]
elif sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
else:
    pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
