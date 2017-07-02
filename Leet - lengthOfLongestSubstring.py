class Solution(object):
    def lengthOfLongestSubstring(self, s):
        word = set()
        maxlength = 0
        length = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in word:
                    word.add(s[j])
                    length = length + 1
                else:
                    break
            if length>maxlength:
                maxlength=length
                #maxstring=word

            word.clear()
            length=0

        print("max length",maxlength)

obj = Solution()
obj.lengthOfLongestSubstring("1")