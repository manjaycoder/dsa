class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:
    def __init__(self):
        self.linked_list = LinkedList() 
    def __str__(self):
        values = [str(node.value) for node in self.linked_list]
        return "\n".join(values)

    def is_empty(self):
        return self.linked_list.head is None  

    def push(self, value):
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def pop(self):
        if self.is_empty():
            return "The stack is empty"
        else:
            value = self.linked_list.head.value
            self.linked_list.head = self.linked_list.head.next
            return value

    def peek(self):
        if self.is_empty():
            return "The stack is empty"
        else:
            return self.linked_list.head.value

    def delete(self):
        self.linked_list.head = None


s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
print("Popped value:", s1.pop())
s1.delete()
print("Stack after deletion:\n", s1)
