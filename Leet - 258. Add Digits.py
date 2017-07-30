class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>=10:
            num=sum(map(int, str(num)))

        print(num)



print(str(45))
obj=Solution()
obj.addDigits(39)
