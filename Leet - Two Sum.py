class sum(object):

    def twosum(data):
        array=[2,7,11,15,2,5,4]
        ptr1=0
        ptr2=1
        flag=False

        while ptr1<len(array)-1:
            for ptr2 in range (ptr1+1,len(array)):
                if (array[ptr1]+array[ptr2])==data:
                    print("number1 is: ")
                    print(array[ptr1])
                    print("number2 is: ")
                    print(array[ptr2])
                    flag=True
            ptr1=ptr1+1
        if flag is False:
            print("Could not find the number set")


    def twoSum2(self, nums, target):    #correct the function names
        map = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in map:
                return [i, map[target - num]]
            else:
                map[num] = i
        return None


sum.twosum(9)