class palindrome(object):

    def palindromecheck1(data):
        string=data
        revdata=data[::-1]

        if string == revdata:
            print(string+" string is palindrome")
        else:
            print(string+" is not palindrome")

    def palindromecheck2(data):
        left=0
        right= len(data) - 1
        flag=True

        while left<right:
            if data[left]== data[right]:
                left=left+1
                right=right-1
            else:
                print("Not Palindrome")
                flag=False
                break

        if flag==True:
            print("Its Palindrome")


palindrome.palindromecheck2("0")

