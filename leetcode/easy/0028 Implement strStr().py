class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        elif needle not in haystack:
            return -1



x = Solution()
x.strStr("hello", "l")