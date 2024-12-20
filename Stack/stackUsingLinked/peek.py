class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Linked:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:
    def __init__(self):
        self.Linked = Linked()  # Correct the usage of Linked list here.

    def __str__(self):
        value = [str(x.value) for x in self.Linked]
        return "\n".join(value)

    def isEmpty(self):
        return self.Linked.head is None  # Simplify the return statement.

    def push(self, value):
        node = Node(value)
        node.next = self.Linked.head
        self.Linked.head = node
    def pop(self):
        if self.isEmpty():
            return "the linked list in stack is empty"
        else:
            temp=self.Linked.head.value
            self.Linked.head=self.Linked.head.next
            return temp
    def peek(self):
        if self.isEmpty():
            return "the linked list in stack is empty"
        else:
            temp=self.Linked.head.value
            
            return temp


s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.pop()
print(s1)
