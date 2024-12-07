class Node:
    def __init__(self,value=None):
        self.value=value
        self.prev=None
        self.next=None
class DoublySLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def createSLL(self,nodeValue):
        node=Node(nodeValue)
        node.prev=None
        node.next=None
        self.head=node
        self.tail=node
    def insertion(self,value,location):
        newNode=Node(value)
        if self.head is None:
            return "the linked list is empty"
        elif location ==0:
            newNode.prev=None
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
        elif location == 1:
            newNode.next=None
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode
        else:
            tempNode=self.head
            index=0
            while index<location-1:
                tempNode=tempNode.next
                index +=1
            newNode.next=tempNode.next
            newNode.prev=tempNode
            newNode.prev.next=newNode
            tempNode.next=newNode
            
            
            

D1=DoublySLL()
D1.createSLL(1)
D1.insertion(2,0)
D1.insertion(2,1)
D1.insertion(3,2)
print([node.value for node in D1])