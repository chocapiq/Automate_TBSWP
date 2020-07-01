listA = []
listB = []
listFinal = []
v = 1

d = int(input())
if 1 > d:
    d = 1
elif d < 10:
    d = 10
else:
    d = d
print(d)
while v <= d:
    a, b = map(int, input().split())
    if a+b >= 1 or a+b <= 1000000000:
        listA.append(a)
        listB.append(b)
        v += 1
    else:
        raise ValueError

def lastDigit(x, y):
    lastDigitList = [x[i]**y[i] for i in range(len(x))]
    for k in lastDigitList:
        q = k%10
        listFinal.append(q)

lastDigit(listA, listB)
for i in listFinal:
    print(i)