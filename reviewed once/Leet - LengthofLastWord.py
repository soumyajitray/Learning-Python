# a=""
# w=a.split()
# print(len(w))


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        array=s.split()
        if len(array)>0:
            print(len(array[-1]))
            return len(array[-1])
        else:
            return 0



obj=Solution()
obj.lengthOfLastWord("I am a good boy")