class Solution(object):
    def fib(self, N):
        n = N
        def F(n):
            if n == 0 or n == 1:
                return n
            else:
                return F(n - 1) + F(n - 2)
        N = F(n)
        print(N)
        return N

x = Solution()
x.fib(6)