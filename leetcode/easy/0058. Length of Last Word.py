class Solution(object):
    def lengthOfLastWord(self, s):
        listOfWords = s.split(" ")
        print(listOfWords)
        while True:
            try:
                if len(listOfWords[-1]) == 0:
                    del listOfWords[-1]
                else:
                    break
            except:
                break
        print(listOfWords)
        if s == []:
            print("0")
            return 0
        print(listOfWords)
        try:
            print(len(listOfWords[-1]))
            return len(listOfWords[-1])
        except:
            print("0")
            return 0



x = Solution()
#x.lengthOfLastWord(" ")
x.lengthOfLastWord("")
x.lengthOfLastWord("Hello World ")
#x.lengthOfLastWord("Hello World")
#x.lengthOfLastWord("Length of the Last Word")