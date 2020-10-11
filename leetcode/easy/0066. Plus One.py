class Solution(object):
    def plusOne(self, digits):
        digits.insert(0, 0)
        minLength = -1 * len(digits)
        index = -1
        if digits[-1] == 9:
            while index >= minLength:
                try:
                    if digits[index] == 9:
                        digits[index] = 0
                    else:
                        digits[index] = digits[index] + 1
                        break
                    index -= 1
                except:
                    break
        else:
            digits[-1] = digits[-1] + 1
        if digits[0] == 0:
            del digits[0]
        print(digits)
        return digits

x = Solution()
x.plusOne([9,9,3,9])
x.plusOne([1,9])
x.plusOne([9])
x.plusOne([1,2,3])
x.plusOne([1,5,6,4,3,2])