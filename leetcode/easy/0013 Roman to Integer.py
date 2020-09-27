def romanToInt(x):
    table = []
    a = 0
    for i in x:
        table.append(i)
    for index, item in enumerate(table):
        if item == "I":
            table[index] = 1
        if item == "V":
            table[index] = 5
        if item == "X":
            table[index] = 10
        if item == "L":
            table[index] = 50
        if item == "C":
            table[index] = 100
        if item == "D":
            table[index] = 500
        if item == "M":
            table[index] = 1000
    c = 0
    table.append(0)
    while a < len(table)-1:
        if table[a] < table[a+1]:
            b = table[a+1] - table[a]
            c += b
            a += 2
        else:
            c += table[a]
            a += 1
    print(c)

romanToInt("III")