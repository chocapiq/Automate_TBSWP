class Solution(object):
    def searchInsert(self, nums, target):
        index = -1
        while index < len(nums):
            index += 1
            if nums[index] == target:
                print(index)
                return index
                break
            elif index == len(nums) - 1:
                if nums[index] > target:
                    print(index)
                    return index
                    break
                else:
                    print(index+1)
                    return index+1
                    break
            elif nums[index] > target:
                print(index)
                return index
                break


x = Solution()
x.searchInsert([1], 0)
'''x.searchInsert([1,3,5,6], 5)
x.searchInsert([1,3,5,6], 4)
x.searchInsert([1,3,5,6], 6)
x.searchInsert([1,3,5,6], 7)
x.searchInsert([1,3,5,6], 0)'''
