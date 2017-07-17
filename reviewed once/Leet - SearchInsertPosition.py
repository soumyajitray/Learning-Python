class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        temp=nums
        l=len(temp)
        i = 0
        if l == 0:
            print('first element')
            return 0
        elif l==1:
            if nums[0]>target:
                return 0
            elif nums[0]==target:
                return 0
            else:
                return 1
        while nums[i] < target and i<len(temp)-1 :
            i = i + 1

        if target>nums[i]:
            return i+1
        else:
            return i



obj = Solution()
obj.searchInsert([1,3], 4)
