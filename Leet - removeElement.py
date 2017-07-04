class Solution(object):
    def removeElement(nums, val):
        counter=0
        if len(nums)>1:
            for i in range(len(nums)-1):
                if nums[i]==val:
                        for j in range(i,len(nums)-1):
                            nums[j]=nums[j+1]
                        ## nums[len(nums)-1]
                        # del nums[len(nums)-1]
                        counter=counter+1
            for element in range(0,counter):
                del nums[len(nums) - 1]

        elif len(nums)==1 and nums[0]==val:
            del nums[0]
        elif len(nums)==1 and nums[0]!=val:
            print(len(nums))
            return len(nums)
        else:
            return 0

        print(len(nums))

Solution.removeElement([3,3],3)

