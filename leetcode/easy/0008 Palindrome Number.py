def palindrome(x):
    table1 = []
    a = 0
    for i in str(x):
        if i != "-":
           table1.append(i)
        else:
           a += 1
    table1.reverse()
    reverseNum = ''.join(table1)
    return(int(x) == int(reverseNum))
    print(reverseNum)
    return int(reverseNum)


palindrome(111)