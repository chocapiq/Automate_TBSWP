def longestCommonPrefix(strs):
    try:
        basePrefix = strs[0]
    except:
        basePrefix = ""
    x = len(basePrefix) - 1
    c = len(strs)
    y = ""
    if len(strs) == 1:
        y = strs[0]
    else:
        while True:
            if c == 0:
                break
            c = len(strs)
            y = ""
            a = basePrefix[0:x]
            for i in strs:
                if a in i[0:x]:
                    c -= 1
                if c == 0:
                    y = a
                    break
            x -= 1
            if x == 0:
                break
    return y
    print(y)


longestCommonPrefix(["c","acc","ccc"])