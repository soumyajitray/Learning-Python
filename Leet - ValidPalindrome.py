import re
class Solution(object):
    def isPalindrome(self, s):

        Strings = re.findall(r'\d+|\w+', s)

        print(Strings)
        teststring=''.join(Strings)
        print(teststring)

        flag=self.palindromecheck1(teststring)
        if flag==True:
            print("string is palindrome")
        else:
            print("String is not palindrome")

    def palindromecheck1(self,data):
        string=data
        revdata=data[::-1]

        if string == revdata:
            return True
        else:
            return False


    def isPalindromeconsolidated(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Strings = re.findall(r'\d+|\w+', s)

        teststring=''.join(Strings)
        test=teststring.lower()
        revdata=test[::-1]

        if test == revdata:
            return True
        else:
            return False

obj=Solution()
obj.isPalindromeconsolidated("A man, a plan,1231 a canal: Panama12313")


