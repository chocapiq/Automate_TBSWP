class Solution(object):
    def addBinary(self, a, b):
        def binToDec(num):
            num = list(str(num))
            print(num)
            index = -1
            decNum = 0
            for i in range(len(num)):
                if num[index] == "0":
                    index -= 1
                    continue
                elif num[index] == "1":
                    decNum = decNum + 2**i
                    index -= 1
            return decNum
        a = binToDec(a)
        b = binToDec(b)
        number = a + b
        n = 0
        k = 1
        bin1 = 2 ** n
        binaryNum = [1]
        if number == 0:
            binaryNum = "0"
        else:
            while bin1 <= number:
                n += 1
                bin1 = 2 ** n
            numberToBin = 2 ** (n - k)
            while numberToBin != number:
                k += 1
                if number < numberToBin + 2 ** (n - k):
                    binaryNum.append("0")
                    continue
                else:
                    numberToBin = numberToBin + 2 ** (n - k)
                    binaryNum.append("1")
            while n != k:
                k += 1
                binaryNum.append("0")
            binaryNum = ''.join(str(v) for v in binaryNum)
        binaryNum = ('"' + str(binaryNum) + '"')
        print(binaryNum)
        return binaryNum



x = Solution()
x.addBinary(101010100101010101, 0)