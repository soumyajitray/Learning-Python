class numbers(object):
    def reversenumbers(x):
        rev=0
        if 2147483647>x>0:
            while x != 0:
                rem=x%10
                rev=rev*10+rem
                x=int(x/10)
        elif -2147483648<x<0:
            while x != 0:
                rem = x % -10
                rev = rev * 10 + rem
                x = int(x / 10)
        else:
            return 0

        print(rev)

numbers.reversenumbers(-123)
