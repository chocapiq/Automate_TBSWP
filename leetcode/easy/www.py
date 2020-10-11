number = 1122
n = 0
k = 1
bin1 = 2**n
binaryNum = [1]
if number == 0:
    numberToBin = 0
else:
    while bin1 <= number:
        n += 1
        bin1 = 2**n
    numberToBin = 2**(n-k)
    while numberToBin != number:
        k += 1
        if number < numberToBin + 2**(n-k):
            binaryNum.append("0")
            continue
        else:
            numberToBin = numberToBin + 2**(n-k)
            binaryNum.append("1")
    while n != k:
        k += 1
        binaryNum.append("0")
    binaryNum = ''.join(str(v) for v in binaryNum)
print(numberToBin)
print(binaryNum)