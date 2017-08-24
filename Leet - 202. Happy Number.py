# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

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