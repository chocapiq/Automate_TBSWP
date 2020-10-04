class Solution(object):
    def removeElement(self, nums, val):
        index = 0
        while index < (len(nums)):
                if nums[index] == val:
                    del nums[index]
                else:
                    index += 1
        return len(nums)

x = Solution()
x.removeElement([1,2,3,3,4],3)