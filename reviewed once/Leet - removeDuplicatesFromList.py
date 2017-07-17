class Solution(object):

    def removeDuplicates(self,nums):

        uniqueset=set()
        for i in range(len(nums)):
            if nums[i] not in uniqueset:
                uniqueset.add(nums[i])
        print(uniqueset)
        print("Length: ")
        print(len(uniqueset))

    def removeDuplicatesWithoutExtraMemory(self,nums):
        w=len(nums)
        count=0
        for i in range(len(nums)):
            if count >= w:
                break
            while nums[i]==nums[i+1]:
                count=count+1
                if count>=w:
                    break
                if nums[i] == nums[i + 1]:

                    for j in range(i,len(nums)-1):
                        nums[j] = nums[j + 1]
                else:
                    i=i+1

        print(i)

obj = Solution()
obj.removeDuplicatesWithoutExtraMemory([1,1,2,3,3,4,4])