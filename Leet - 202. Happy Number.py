class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        word = set()

        while n!=1:

            n=sum(map(self.square, str(n)))
            if n not in word:
                word.add(n)
            else:
                return False
                break
        print(n)
        return True

    def square(self, n):
        res = int(n) * int(n)
        return res




obj=Solution()
obj.isHappy(2)