class solution(object):


    def validparentheses(self,s):
        array=s
        i=0
        j=0
        k=0
        b= True

        if len(array)>1:
            for l in range(0,len(array)):

                if i>=0 and j>=0 and k>=0:
                    if  array[l]=='[':
                        i=i+1
                    elif array[l]==']':
                        i=i-1

                    if  array[l]=='{':
                        j=j+1
                    elif array[l]=='}':
                        j=j-1

                    if  array[l]=='(':
                        k=k+1
                    elif array[l]==')':
                        k=k-1

                else:
                    print("Not valid Parenthesis")
                    #b= False
                    return False
                    #break;
        elif len(array)==0:
            print("valid Parenthesis")
            return True
        else:
            print("Not valid Parenthesis")
            return False
        print("Not valid Parenthesis")

        if i==0 and j==0 and k==0:
            return True
        else:
            return False

    def validparentheses2(self,s):

obj=solution()
obj.validparentheses("{")