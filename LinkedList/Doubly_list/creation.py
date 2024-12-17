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
    
            
            
            

D1=DoublySLL()
D1.createSLL(1)

print([node.value for node in D1])