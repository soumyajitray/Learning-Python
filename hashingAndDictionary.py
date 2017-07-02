class abstract(object):

    def hashfunction(self,key):
        sum=0
        for pointer in range(len(key)):
            sum=sum+ord(key[pointer])
        return  sum%self.size

    def put(self,key,data):
        index=self.hashfunction(key)
        while self.key[index] is not None:
            if self.key[index]==key:
                

