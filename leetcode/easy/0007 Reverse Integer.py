def reverse(x):
    if x <= pow(-2, 31) or x > pow(2, 31):
        x = 0
    table1 = []
    a = 0
    for i in str(x):
        if i != "-":
           table1.append(i)
        else:
           a += 1
    table1.reverse()
    while True:
        if len(table1) == 1:
            break
        if table1[0] == '0':
            del table1[0]
        else:
            break
    if a != 0:
        table1.insert(0, '-')
    reverseNum = ''.join(table1)
    if int(reverseNum) <= pow(-2, 31) or int(reverseNum) > pow(2, 31):
        reverseNum = 0
    print(reverseNum)
    return int(reverseNum)


reverse(11534236469)