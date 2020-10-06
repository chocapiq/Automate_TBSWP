class Solution(object):
    def countAndSay(self, n):
        x = str(1)
        if n == 1:
            return x
        else:
            for i in range(n-1):
                x = (x + '0')
                index = 0
                y = []
                z = []
                listFinal = []
                str1 = ""
                while index < len(x) - 1:
                    if x[index] == x[index+1]:
                        y.append(x[index])
                        index += 1
                    else:
                        y.append(x[index])
                        str1 = str1.join(y)
                        z.append(str1)
                        y = []
                        str1 = ""
                        index += 1
                for i in z:
                    lengthOfSingleValue = len(i)
                    listFinal.append(lengthOfSingleValue)
                    listFinal.append(i[0])

                strFinal = ''.join(str(k) for k in listFinal)
                x = strFinal
            return strFinal

x = Solution()
x.countAndSay(2)