class Queue (object):
    def __init__(self):
        self.Queue=[]
    def isEmpty(self):
        return self.Queue == []
    def addQueue(self,data):
        self.Queue.append(data)
    def delQueue(self):
        data = self.Queue[0]
        del self.Queue[0]
        return data
    def sizeQueue(self):
        return len(self.Queue)