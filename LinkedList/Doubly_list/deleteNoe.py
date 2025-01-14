class Node:
    def __init__(self, value=None):
        self.value = value  # Initialize the node's value
        self.prev = None  # Initialize the pointer to the previous node as None
        self.next = None  # Initialize the pointer to the next node as None

class DoublySLL:
    def __init__(self):
        self.head = None  # Initialize the head of the Doubly Singly Linked List (DSLL)
        self.tail = None  # Initialize the tail of the DSLL

    def __iter__(self):
        node = self.head
        while node:
            yield node  # Yield the current node to enable iteration
            node = node.next  # Move to the next node

    def createSLL(self, nodeValue):
        node = Node(nodeValue)  # Create a new node with the given value
        node.prev = None  # Set the previous pointer to None
        node.next = None  # Set the next pointer to None
        self.head = node  # Set the new node as the head
        self.tail = node  # Set the new node as the tail

    def insertion(self, value, location):
        newNode = Node(value)  # Create a new node with the given value
        if self.head is None:  # Check if the list exists
            return "The linked list is empty"
        elif location == 0:  # Insert at the beginning
            newNode.prev = None  # Set the previous pointer of the new node to None
            newNode.next = self.head  # Point the new node's next to the current head
            self.head.prev = newNode  # Update the current head's previous pointer
            self.head = newNode  # Update the head to the new node
        elif location == 1:  # Insert at the end
            newNode.next = None  # Set the next pointer of the new node to None
            newNode.prev = self.tail  # Point the new node's previous to the current tail
            self.tail.next = newNode  # Update the current tail's next pointer
            self.tail = newNode  # Update the tail to the new node
        else:  # Insert at a specific location
            tempNode = self.head  # Start from the head
            index = 0  # Initialize index
            while index < location - 1:  # Traverse to the node before the target location
                tempNode = tempNode.next
                index += 1
            newNode.next = tempNode.next  # Point the new node's next to the next node
            newNode.prev = tempNode  # Point the new node's previous to the current node
            if tempNode.next:  # Update the next node's previous pointer if it exists
                tempNode.next.prev = newNode
            tempNode.next = newNode  # Update the current node's next pointer

    def Searching(self, value):
        if self.head is None:  # Check if the list is empty
            print("The linked list is empty")
            return
        else:
            tempNode = self.head  # Start from the head
            while tempNode:
                if tempNode.value == value:  # Check if the current node contains the value
                    return tempNode.value  # Return the value if found
                tempNode = tempNode.next  # Move to the next node
            return "The linked list item is not present"  # Return if the value is not found

    def delete(self, Location):
        if self.head is None:  # Check if the list is empty
            print("The linked list is empty")
        else:
            if Location == 0:  # Deletion at the beginning
                if self.head == self.tail:  # If there's only one node
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next  # Update the head to the next node
                    self.head.prev = None  # Remove the previous pointer of the new head
            elif Location == 1:  # Deletion at the end
                if self.head == self.tail:  # If there's only one node
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev  # Update the tail to the previous node
                    self.tail.next = None  # Remove the next pointer of the new tail
            else:  # Deletion at a specific location
                currNode = self.head  # Start from the head
                index = 0  # Initialize index
                while index < Location - 1:  # Traverse to the node before the target location
                    currNode = currNode.next
                    index += 1
                currNode.next = currNode.next.next  # Update the next pointer to skip the target node
                if currNode.next:  # Update the previous pointer of the next node if it exists
                    currNode.next.prev = currNode

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
