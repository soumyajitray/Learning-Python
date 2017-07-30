class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=nums[0]
        for i in range(len(nums)-1):
            temp=temp ^ nums[i+1]

        print(temp)

obj=Solution()
obj.singleNumber([1,1,2,2,4,5,4,5,6])