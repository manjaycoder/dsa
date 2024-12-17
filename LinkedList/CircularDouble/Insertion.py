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

    def Insertion(self, value, location):
        # Method to insert a new node into the circular doubly linked list
        if self.head is None:
            # If the list is empty, return an error message
            return "The linked list is empty"
        else:
            newNode = Node(value)  # Create a new node with the given value
            if location == 0:  # Insert at the beginning
                newNode.next = self.head  # Point newNode's next to the current head
                newNode.prev = self.tail  # Point newNode's prev to the tail
                self.head.prev = newNode  # Update current head's prev to point to newNode
                self.head = newNode  # Update the head to the newNode
                self.tail.next = newNode  # Update the tail's next to maintain circular link
            elif location == 1:  # Insert at the end
                newNode.next = self.head  # Point newNode's next to the head (circular link)
                newNode.prev = self.tail  # Point newNode's prev to the current tail
                self.tail.next = newNode  # Update current tail's next to newNode
                self.tail = newNode  # Update the tail to the newNode
                self.head.prev = newNode  # Update the head's prev to maintain circular link
            else:  # Insert at a specific location
                tempNode = self.head  # Start from the head
                index = 0
                while index < location - 1 and tempNode.next != self.head:
                    # Traverse the list to find the position for insertion
                    tempNode = tempNode.next
                    index += 1
                # Insert the new node between tempNode and tempNode.next
                newNode.next = tempNode.next  # Point newNode's next to tempNode's next
                newNode.prev = tempNode  # Point newNode's prev to tempNode
                tempNode.next.prev = newNode  # Update next node's prev to newNode
                tempNode.next = newNode  # Update tempNode's next to newNode
        return "The node has been successfully inserted"

# Create an instance of the CircularDoubly linked list
custom = CircularDoubly()

# Create the circular doubly linked list with an initial value of 9
print(custom.Creation(9))

# Insert nodes at different positions
print(custom.Insertion(5, 0))  # Insert 5 at the beginning
print(custom.Insertion(15, 1))  # Insert 15 at the end
print(custom.Insertion(7, 1))  # Insert 7 at a specific location (after the first node)

# Print the values of the circular doubly linked list
print([node.value for node in custom])  # [5, 9, 7, 15]
