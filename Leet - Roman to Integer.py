class Solution(object):
# @param {string} s
# @return {integer}
    def romanToInt(self, s):
        romandictionary={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        temp=0
        for i in range(len(s)-1):

            # print(romandictionary[s[i]])
            # print(romandictionary[s[i + 1]])
            if romandictionary[s[i]]>=romandictionary[s[i+1]]:
                # print(s[i])
                # print(romandictionary[s[i+1]])
                temp=romandictionary[s[i]]+temp
            elif romandictionary[s[i]]<romandictionary[s[i+1]]:
                temp=temp-romandictionary[s[i]]
                # print(s[i])
                # print(romandictionary[s[i+1]])
        temp=temp+romandictionary[s[-1]]
        print(temp)

obj=Solution()
obj.romanToInt("IX")