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
    def Searching(self,value):
        if self.head is None:
            priint("the linked list is empty")
        else:
            tempNode=self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value 
                tempNode=tempNode.next
            return "the linked list etiem is not present"
    def delete(Self,Location):
        if self.head is None:
            print("the linked list is empty")
        else:
            if Location == 0:
                if self.head == self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None
            if Location == 1:
                if self.head == self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                currNode=self.head
                index = 0
            while index < Location -1:
                currNode=currNode.next
                index+=1
            currNode.next=currNode.next.next
            currNode.next.prev=currNode
        print("the item is not found")


D1=DoublySLL()
D1.createSLL(1)
D1.insertion(2,0)
D1.insertion(2,1)
D1.insertion(3,2)
print(D1.Searching(3))
print([node.value for node in D1])