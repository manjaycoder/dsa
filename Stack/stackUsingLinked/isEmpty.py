class Node:
    def __init__(self,value=None):
        self.value=None
        self.next=None
class Linked:
    def __init__(self):
        self.head=None
class Stack:
    def __init__(self):
        self.Linked=Linked()
    def isEmpty(self):
        if self.Linked.head is None:
            return True
        else:
            return False
s1=Stack()
print(s1.isEmpty())
    