import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        PrimeCount=0
        # j=0
        primelist=[]
        for i in range(2,n):
            if self.primeCheck1(i,primelist)==True:
                primelist.append(i)       #try2 with new logic
                PrimeCount=PrimeCount+1
        print(PrimeCount)       #try2 with new logic
        print(primelist)       #try2 with new logic
        return PrimeCount
    #
    # def primeCheck(self,n):
    #     flag=False
    #     if n==2:
    #         return True
    #     elif n==3:
    #         return True
    #     sqroot=int(math.sqrt(n))
    #     for i in range(2,sqroot+1):
    #         if n%i==0:
    #             flag=True
    #
    #     if flag!=True:
    #         return True
    #     else:
    #         return False



    def primeCheck1(self,n,primelist):
        flag=False
        if n==2:
            # print("prime")
            return True
        elif n==3:
            # print("prime")
            return True
        sqroot=int(math.sqrt(n))

        for j in range(0,sqroot):
            if n%primelist[j]==0:
                flag=True
                # print("not prime")
                break

        if flag!=True:
            # print("prime")
            return True
        else:
            return False



obj=Solution()
obj.countPrimes(499979)