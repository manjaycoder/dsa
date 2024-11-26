class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class SLinkd_list:
    def __init__(self):
        self.head=None;
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def insert(self,value,location):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            if location == 0:
                newNode.next=self.head
                self.head=newNode
            elif location == 1:
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index = 0
                while index < location -1:
                    tempNode=tempNode.next
                    index +=1
                nextNode=tempNode.next
                tempNode.next=newNode


single=SLinkd_list()
single.insert(1,1)
single.insert(2,1)
single.insert(3,1)
single.insert(4,1)
single.insert(5,1)
single.insert(0,0)
single.insert(6,1)
print([node.value for node in single])