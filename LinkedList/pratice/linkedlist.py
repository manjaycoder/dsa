from random import randint

class Node:
    def __init__(self, value=None):
        # Initialize a node with a value, next pointer, and previous pointer
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        # Return the string representation of the node's value
        return str(self.value)

class LinkedList:
    def __init__(self):
        # Initialize the linked list with head and tail pointers
        self.head = None
        self.tail = None

    def __iter__(self):
        # Make the linked list iterable
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def __str__(self):
        # Return a string representation of the linked list by joining node values
        values = [str(node.value) for node in self]
        return "->".join(values)

    def __len__(self):
        # Return the length of the linked list by counting nodes
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next
        return length

    def add(self, value):
        # Add a new node with the given value to the end of the list
        new_node = Node(value)
        if self.head is None:
            # If the list is empty, set head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, append the new node to the tail
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node

    def generate(self, n, min_value, max_value):
        # Generate a linked list with 'n' random values in the range [min_value, max_value]
        self.head = None
        self.tail = None
        for _ in range(n):
            self.add(randint(min_value, max_value))
        return self

# Example usage
custom_list = LinkedList()
custom_list.generate(10, 1, 9)

