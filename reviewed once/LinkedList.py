# -*- coding: UTF-8 -*-

class node(object):
    def __init__(self, data):
        self.data=data
        self.next=None

class  LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0
    def insertstart(self,data):
        self.size=self.size+1
        newNode= node(data)

        if not self.head:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode

    def size1(self):
        # print("came here")
        return self.size

    def insertend(self,data):
        self.size=self.size+1
        newNode=node(data)
        actualnode=self.head
        while actualnode.next is not None:
            actualnode=actualnode.next
        actualnode.next=newNode

    def traverselist(self):
        currNode=self.head
        while currNode is not None:
            print("%d" % currNode.data)
            currNode=currNode.next

    def remove(self, data):
        if self.head is None:
            return

        pointer_node = self.head
        previous_node = None
        found = False

        if pointer_node.data == data:
            self.head = pointer_node.next

        while pointer_node is not None:
            if pointer_node.data == data:
                found = True
                previous_node.next = pointer_node.next
                self.size -= 1
                break
            else:
                previous_node = pointer_node
                pointer_node = pointer_node.next

        if found:
            print("delted data")
        else:
            print("data not found")
    # def remove(self,data):
    #     if self.head is None:
    #         return
    #     self.size=self.size-1
    #     currNode=self.head
    #     prevNode=None
    #     flag=False
    #     while currNode is not None and currNode.data is not data:
    #         prevNode=currNode
    #         currNode=currNode.next
    #
    #     if prevNode is None:
    #         self.head=currNode.next
    #         flag=True
    #     else:
    #         prevNode.next=currNode.next
    #         flag=True