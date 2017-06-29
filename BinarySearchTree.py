class Node(object):

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class binarySearchTree(object):

    def __init__(self):
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self.insertNode(data, self.root)

# O(log N) as long as tree is bananced

    def insertNode(self,data,node):
        if data < node.data:
            if node.left:
                self.insertNode(data, node.left)
            else:
                node.left=Node(data)
        else:
            if node.right:
                self.insertNode(data, node.right)
            else:
                node.right=Node(data)


    def getminvalue(self):
        if self.root:
            return self.getmin(self.root)
    def getmin(self,node):
        if node.left:
            return self.getmin(node.left)
        return node.data


    def getmaxvalue(self):
        if self.root:
            return self.getmax(self.root)
    def getmax(self, node):
        if node.right:
            return self.getmax(node.right)
        return node.data

    def remove(self,data):
        if self.root:
            self.root = self.removenode(data, self.root)
    def removenode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.left=self.removenode(data,node.left)

        elif data > node.data:
            node.right=self.removenode(data,node.right)

        else:
            if not node.left and not node.right:
                print("removing a leaf node", node.data)
            del node
            return None

        if not node.left:
            print("removing a node with single right child")
            temp=node.right
            del node
            return temp

        elif not node.right:
            print("removing a node with single left child")
            temp=node.left
            del node
            return temp
        print("Removing Node with two children")
        temp=self.Predececessor(node.left)
        node.data=temp.data
        node.left=self.removeNode(temp.data,node.left)

        return node


    def traverse(self):
        if self.root:
            return self.inorder(self.root)
    def inorder(self,node):
        # if node is None:
        #     return
        # else:
        #     self.inorder(node.left)
        #     print(node.data)
        #     self.inorder(node.right)
        if node.left:
            self.inorder(node.left)

        print(node.data)

        if node.right:
            self.inorder(node.right)


bst= binarySearchTree()
bst.insert(12)
bst.insert(6)
bst.insert(14)
bst.insert(2)
bst.insert(7)
bst.insert(13)
bst.insert(14)
bst.insert(15)

#print(bst.getminvalue())
#print(bst.getmaxvalue())
print(bst.traverse())