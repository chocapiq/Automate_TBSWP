class Solution(object):
    def maxSubArray(self, nums):
        maxValue = currentValue = nums[0]
        x = 1
        while x < len(nums):
            print(str(currentValue) + str(" kappa"))
            currentValue = max(nums[x], currentValue + nums[x])
            print(str(currentValue) + str(" 2"))
            if currentValue > maxValue:
                maxValue = currentValue
            x += 1
        print(maxValue)
        return maxValue

x = Solution()
x.maxSubArray([-2,-1])
x.maxSubArray([1,2,-1,-3,2,1,-2,1,4,-5,4])
x.maxSubArray([43,1,-3,4,-1,2,-1,5,4])
x.maxSubArray([0,1,-3,4,-1,2,-1,5,4])
x.maxSubArray([0,-1,-2,-3,7,-2,-4])
x.maxSubArray([1,1,1,-7,5,-7,-4])