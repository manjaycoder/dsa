class Node:
    # Node class to represent an individual element in the circular doubly linked list
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
        # Iterator to traverse through the circular doubly linked list
        node = self.head  # Start from the head
        while node:
            yield node  # Yield the current node
            node = node.next  # Move to the next node
            if node == self.head:  # Stop iteration when we return to the head
                break

    def Creation(self, nodeValue):
        # Create the circular doubly linked list with one node
        node = Node(nodeValue)  # Create a new node with the given value
        self.head = node  # Set the head pointer to the new node
        self.tail = node  # Set the tail pointer to the new node
        node.next = node  # The node points to itself (circular link)
        node.prev = node  # The node points to itself (circular link)
        return "The circular doubly linked list is created"

    def Insertion(self, value, location):
        # Insert a new node into the circular doubly linked list
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
                    # Traverse to the position for insertion
                    tempNode = tempNode.next
                    index += 1
                # Insert the new node between tempNode and tempNode.next
                newNode.next = tempNode.next  # Point newNode's next to tempNode's next
                newNode.prev = tempNode  # Point newNode's prev to tempNode
                tempNode.next.prev = newNode  # Update next node's prev to newNode
                tempNode.next = newNode  # Update tempNode's next to newNode
        return "The node has been successfully inserted"

    def traverse(self):
        # Traverse and print all the elements in the list
        if self.head is None:
            print("The linked list is empty")
        else:
            tempNode = self.head  # Start from the head
            while True:
                print(tempNode.value, end=" -> ")  # Print the current node's value
                if tempNode == self.tail:  # Stop traversal at the tail
                    break
                tempNode = tempNode.next  # Move to the next node
            print("(Back to Head)")  # Indicate the circular nature

    def traverseReverse(self):
        # Traverse the list in reverse order
        if self.head is None:
            print("The linked list is empty")
        else:
            tempNode = self.tail  # Start from the tail
            while True:
                print(tempNode.value, end=" -> ")  # Print the current node's value
                if tempNode == self.head:  # Stop traversal at the head
                    break
                tempNode = tempNode.prev  # Move to the previous node
            print("(Back to Tail)")  # Indicate the circular nature

    def Searching(self, value):
        # Search for a node with the given value
        if self.head is None:
            return "The linked list is empty"
        else:
            tempNode = self.head  # Start from the head
            while True:
                if tempNode.value == value:  # Value is found
                    return f"Value {value} found in the list"
                if tempNode == self.tail:  # Reached the tail; value not found
                    return f"Value {value} not found in the list"
                tempNode = tempNode.next  # Move to the next node

    def delete(self, location):
        # Delete a node from the list
        if self.head is None:
            print("The linked list is empty")
        else:
            if location == 0:  # Delete from the beginning
                if self.head == self.tail:  # Only one node in the list
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next  # Update head to the next node
                    self.head.prev = self.tail  # Update the head's prev to tail
                    self.tail.next = self.head  # Update the tail's next to head
            elif location == 1:  # Delete from the end
                if self.head == self.tail:  # Only one node in the list
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev  # Update tail to the previous node
                    self.tail.next = self.head  # Update tail's next to head
                    self.head.prev = self.tail  # Update head's prev to tail
            else:  # Delete at a specific location
                tempNode = self.head  # Start from the head
                index = 0
                while index < location - 1 and tempNode.next != self.head:
                    # Traverse to the node before the target
                    tempNode = tempNode.next
                    index += 1
                # Update links to remove the target node
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode

# Example usage
custom = CircularDoubly()
print(custom.Creation(9))
print(custom.Insertion(5, 0))
print(custom.Insertion(15, 1))
print(custom.Insertion(7, 1))
custom.traverse()
custom.traverseReverse()
print(custom.Searching(7))
custom.delete(1)
custom.traverse()
