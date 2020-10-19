class Solution(object):
    def maxProfit(self, prices):
        maxPrice = 0
        for i in range(len(prices)-1):
            n = 1
            if prices[i] < prices[i + n]:
                maxPrice += prices[i + n] - prices[i]
        print(maxPrice)

x = Solution()
x.maxProfit([1,2])
x.maxProfit([1,2,3,4,5])
x.maxProfit([7,1,5,3,6,4])
x.maxProfit([7,1,5,3,6,4])
x.maxProfit([0,4,1,2,3,1,1])
x.maxProfit([4,10,11,8,5,3,1])
x.maxProfit([7,6,4,3,1])

