class Solution(object):
    def mySqrt(self, n):
        if n == 0:
            return 0
        elif n < 10000000:
            for i in range(n)[1::]:
                if i ** 2 > n:
                    k = i
                    break
            for v in range(25):
                k = 1 / 2 * (k + (n / k))
            n = k
            print(int(n))
        else:
            k = 1000
            for v in range(25):
                k = 1/2*(k+(n/k))
            n = k
            print(int(n))

x = Solution()
x.mySqrt(2147395599)
x.mySqrt(10)
x.mySqrt(20)
x.mySqrt(100)
