class Node:
    # Node class to represent an individual element in the linked list
    def __init__(self, value):
        self.value = value  # The value of the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class CircularDoubly:
    def __init__(self):
        # Initialize the circular doubly linked list
        self.head = None  # Head pointer for the list
        self.tail = None  # Tail pointer for the list

    def __iter__(self):
        # Iterating through the circular doubly linked list
        node = self.head
        while node:
            yield node  # Yield the current node
            node = node.next  # Move to the next node
            if node == self.head:  # Stop iteration when we return to the head
                break

    def Creation(self, nodeValue):
        # Method to create the circular doubly linked list with one node
        node = Node(nodeValue)  # Create a new node with the given value
        self.head = node  # Set head to the new node
        self.tail = node  # Set tail to the new node
        node.next = node  # Point the node's next to itself (circular link)
        node.prev = node  # Point the node's prev to itself (circular link)
        return "The circular doubly linked list is created"

# Create an instance of the CircularDoubly linked list
custom = CircularDoubly()

# Create the circular doubly linked list with an initial value of 9
print(custom.Creation(9))

# Print the values of the circular doubly linked list
print([node.value for node in custom])
