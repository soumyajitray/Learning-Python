class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0

        minprice = max(prices)
        maxprofit = 0

        for i in range(len(prices)):
            if (prices[i] < minprice):
                minprice = prices[i]
            elif (prices[i] - minprice > maxprofit):
                maxprofit = prices[i] - minprice
        print (maxprofit)
        return maxprofit;

obj=Solution()
obj.maxProfit([])