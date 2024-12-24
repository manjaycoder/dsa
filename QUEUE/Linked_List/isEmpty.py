class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)
class Linked:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        currNode=self.head
        while currNode:
            yield currNode
            currNode=currNode.next
class Queue:
    def __init__(self):
        self.Linked=Linked()
    def __str__(self):
        values=[str(x) for x in self.Linked ]
        return ' '.join(values)
    def enqueue(self,value):
        newNode=Node(value)
        if self.Linked.head is None:
            self.Linked.head=newNode
            self.Linked.tail=newNode
        else:
            self.Linked.tail.next=newNode
            self.Linked.tail=newNode
    def isEmpty(self):
        if self.Linked.head is None:
            return True
        else:
            return False