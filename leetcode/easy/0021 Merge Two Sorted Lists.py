def mergeTwoLists(l1, l2):
    num1 = 0
    num2 = 0
    for a in l1:
        if a > num1:
            num1 = a

    l1 = sorted(l1)
    l2 = sorted(l2)
    l3 = []
    i1 = -1
    i2 = 0
    if len(l1) >= len(l2):
        alt1 = l1
        alt2 = l2
    else:
        alt1 = l2
        alt2 = l1
    while i1 < len(alt1):
        i1 += 1
        while i1 <= len(alt1):
            if i1 == len(alt1):
                while i2 < len(alt2):
                    l3.append(alt2[i2])
                    i2 += 1
            if i2 == len(alt2):
                break
            if alt1[i1] <= alt2[i2]:
                l3.append(alt1[i1])
                i1 += 1
            else:
                l3.append(alt2[i2])
                i2 += 1


    print(l1)
    print(l2)
    print(l3)
mergeTwoLists([1,2,4],[1,3,4])
mergeTwoLists([12,3,33],[14,4,2,5,11])
mergeTwoLists([4,2,5,11],[12,3,33])