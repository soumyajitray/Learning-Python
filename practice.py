# -*- coding: UTF-8 -*-

from LinkedList import LinkedList

linkedList=LinkedList()
linkedList.insertstart(12)
linkedList.insertstart(122)
linkedList.insertstart(13)
linkedList.insertstart(4)
linkedList.insertstart(25)
linkedList.insertstart(28)
linkedList.insertstart(29)
linkedList.insertend(126)
#linkedList.traverselist()

#29 28 25 4  13 122    12   126

print(linkedList.size1())
linkedList.remove(12)
print(linkedList.size1())
#linkedList.traverselist()