class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class CircularSLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node=node.next
    def creation(self,nodevalue):
        node=Node(nodevalue)
        node.next=self.head
        self.head=node
        self.tail=node
    def insert(self,value,location):
        if self.head is None:
            return "fuck off"
        else:
            newNode=Node(value)
            if location == 0:
                newNode.next=self.head
                self.head=newNode
                self.tail=newNode
            elif location == 1:
                newNode.next=self.tail.next
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index < location -1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode

C1=CircularSLL()
C1.creation(1)

C1.insert(1,0)
C1.insert(2,1)
C1.insert(3,2)
C1.insert(4,3)
print([node.value for node in C1])