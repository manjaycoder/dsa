class Node:
    def __init__(self, value=None):
        self.value = value  # Initialize the node's value
        self.prev = None  # Initialize the pointer to the previous node as None
        self.next = None  # Initialize the pointer to the next node as None

class DoublySLL:
    def __init__(self):
        self.head = None  # Initialize the head of the Doubly Linked List
        self.tail = None  # Initialize the tail of the Doubly Linked List

    def __iter__(self):
        node = self.head  # Start iteration from the head
        while node:
            yield node  # Yield the current node for iteration
            node = node.next  # Move to the next node

    def createSLL(self, nodeValue):
        # Create a new node with the given value
        node = Node(nodeValue)
        node.prev = None  # Set the previous pointer to None
        node.next = None  # Set the next pointer to None
        self.head = node  # Set the new node as the head
        self.tail = node  # Set the new node as the tail

    def insertion(self, value, location):
        # Create a new node with the given value
        newNode = Node(value)
        if self.head is None:  # If the list does not exist
            return "The linked list is empty"
        elif location == 0:  # Insert at the beginning
            newNode.prev = None  # New node's prev is None
            newNode.next = self.head  # Point new node's next to the current head
            self.head.prev = newNode  # Update the current head's prev pointer
            self.head = newNode  # Update the head to the new node
        elif location == 1:  # Insert at the end
            newNode.next = None  # New node's next is None
            newNode.prev = self.tail  # Point new node's prev to the current tail
            self.tail.next = newNode  # Update the current tail's next pointer
            self.tail = newNode  # Update the tail to the new node
        else:  # Insert at a specific location
            tempNode = self.head  # Start traversal from the head
            index = 0  # Initialize index
            while index < location - 1:  # Traverse to the node before the target location
                tempNode = tempNode.next
                index += 1
            newNode.next = tempNode.next  # Point new node's next to tempNode's next
            newNode.prev = tempNode  # Point new node's prev to tempNode
            if tempNode.next:  # If tempNode's next exists
                tempNode.next.prev = newNode  # Update its prev to newNode
            tempNode.next = newNode  # Update tempNode's next to newNode

    def Searching(self, value):
        if self.head is None:  # Check if the list is empty
            return "The linked list is empty"
        tempNode = self.head  # Start from the head
        while tempNode:
            if tempNode.value == value:  # If the current node matches the value
                return tempNode.value  # Return the value
            tempNode = tempNode.next  # Move to the next node
        return "The linked list item is not present"  # Value not found

    def delete(self, location):
        if self.head is None:  # If the list is empty
            print("The linked list is empty")
        else:
            if location == 0:  # Delete the first node
                if self.head == self.tail:  # If there's only one node
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next  # Update head to the next node
                    self.head.prev = None  # Remove the prev pointer of the new head
            elif location == 1:  # Delete the last node
                if self.head == self.tail:  # If there's only one node
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev  # Update tail to the previous node
                    self.tail.next = None  # Remove the next pointer of the new tail
            else:  # Delete a node at a specific location
                currNode = self.head  # Start from the head
                index = 0  # Initialize index
                while index < location - 1:  # Traverse to the node before the target location
                    currNode = currNode.next
                    index += 1
                currNode.next = currNode.next.next  # Update next to skip the target node
                if currNode.next:  # If the next node exists
                    currNode.next.prev = currNode  # Update its prev to currNode

# Example usage:
D1 = DoublySLL()
D1.createSLL(1)  # Create the list with a single node (1)
D1.insertion(2, 0)  # Insert 2 at the beginning
D1.insertion(2, 1)  # Insert 2 at the end
D1.insertion(3, 2)  # Insert 3 at position 2

# Searching for a node
print(D1.Searching(3))  # Output the result of searching for value 3

# Using iteration (list comprehension)
print([node.value for node in D1])  # Output the list of node values
