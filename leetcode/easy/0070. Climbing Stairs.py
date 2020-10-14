class Solution(object):
    def climbStairs(self, n):
        stairsA = 1
        stairsB = 1
        x = 2
        if n == 1:
            stairs = 1
        else:
            while x <= n:
                stairs = stairsA + stairsB
                stairsB = stairsA
                stairsA = stairs
                x += 1
        return stairs

x = Solution()
x.climbStairs(1)
x.climbStairs(2)
x.climbStairs(3)
x.climbStairs(4)
x.climbStairs(5)
x.climbStairs(6)
x.climbStairs(7)