tableData = [['apples', 'oranges', 'cherries', 'banana', 'strawberries'],
             ['Alice', 'Bob', 'Carol', 'David', 'Timothy'],
             ['dogs', 'cats', 'moose', 'goose', 'elephant'],
             ['garlic-dogs', 'pasta', 'tuna', 'rolls', 'rice']]
def tablePrinter(table):
    x = 0
    y = 0
    z = 1
    v = 0
    w = 0
    wordLength1 = []
    gridX = len(table)
    gridY = len(table[1])

    while w < gridX:
        wordLength1.append(0)
        w += 1
    while v < gridX:
        for i in table[v]:
            if wordLength1[v] < len(i):
                del wordLength1[v]
                wordLength1.insert(v, len(i))
        v += 1

    while x <= gridX + 1:
        if x == gridX:
            x = 0
            y += 1
            while y <= gridY:
                if z == 1:
                    print(' ', end='\n')
                if x == gridX or y == gridY:
                    z = 1
                    break
                else:
                    print(table[x][y].rjust(wordLength1[x], ' '), end=' ')
                    x += 1
                    z += 1

        elif y < gridY:
            print(table[x][y].rjust(wordLength1[x], ' '), end=' ')
            x += 1
        else:
            break



tablePrinter(tableData)