class Node:
    def __init__(self, value):
        self.value = value  # Initialize the node's value
        self.next = None  # Initialize the pointer to the next node as None

class Circular:
    def __init__(self):
        self.head = None  # Initialize the head of the Circular Linked List (CLL)
        self.tail = None  # Initialize the tail of the CLL

    def __iter__(self):
        node = self.head
        while node:
            yield node  # Yield the current node to enable iteration
            if node.next == self.tail.next:  # Stop when we circle back to the head
                break
            node = node.next  # Move to the next node

    def Creation(self, nodeValue):
        node = Node(nodeValue)  # Create a new node with the given value
        node.next = node  # Point the node to itself, forming a single-node CLL
        self.head = node  # Set this node as the head of the CLL
        self.tail = node  # Set this node as the tail of the CLL
        return "The CLL has been created"

    def Insertion(self, value, location):
        if self.head is None:  # Check if the CLL exists
            return "The CLL does not exist"
        else:
            newNode = Node(value)  # Create a new node with the given value
            if location == 0:  # Insertion at the beginning of the CLL
                newNode.next = self.head  # Point the new node to the current head
                self.head = newNode  # Update the head to the new node
                self.tail.next = newNode  # Update the tail's next to point to the new head
            elif location == -1:  # Insertion at the end of the CLL
                newNode.next = self.tail.next  # Point the new node to the current head (circular link)
                self.tail.next = newNode  # Update the current tail's next to the new node
                self.tail = newNode  # Update the tail to the new node
            else:  # Insertion at a specific location
                tempNode = self.head  # Start from the head
                index = 0  # Initialize the index
                while index < location - 1:  # Traverse to the node before the target location
                    tempNode = tempNode.next  # Move to the next node
                    index += 1  # Increment the index
                nextNode = tempNode.next  # Store the node currently at the target location
                tempNode.next = newNode  # Point the current node to the new node
                newNode.next = nextNode  # Point the new node to the next node in the sequence
class Node:
    def __init__(self, value):
        self.value = value  # Initialize the node's value
        self.next = None  # Initialize the pointer to the next node as None

class CircularSLL:
    def __init__(self):
        self.head = None  # Initialize the head of the Circular Singly Linked List (CSLL)
        self.tail = None  # Initialize the tail of the CSLL
    
    def __iter__(self):
        node = self.head
        if node:
            while True:
                yield node  # Yield the current node to enable iteration
                node = node.next  # Move to the next node
                if node == self.head:  # Stop if we have looped back to the head
                    break
    
    def creation(self, node_value):
        new_node = Node(node_value)  # Create a new node with the given value
        self.head = new_node  # Set the new node as the head
        self.tail = new_node  # Set the new node as the tail
        self.tail.next = self.head  # Circular reference to make it a CSLL
    
    def insert(self, value, location):
        if self.head is None:  # Check if the list exists
            return "The list is empty, cannot insert."
        
        new_node = Node(value)  # Create a new node with the given value
        
        # Insert at the beginning (location 0)
        if location == 0:
            new_node.next = self.head  # Point new node to the current head
            self.head = new_node  # Update the head to the new node
            self.tail.next = self.head  # Maintain circular linkage
            
        # Insert at the end (location 1)
        elif location == 1:
            new_node.next = self.head  # Point new node to the head
            self.tail.next = new_node  # Update the current tail's next to the new node
            self.tail = new_node  # Update the tail to the new node
            
        else:  # Insert at a specific location
            temp_node = self.head  # Start from the head
            index = 0  # Initialize index
            # Traverse to the node before the target location
            while index < location - 1 and temp_node.next != self.head:
                temp_node = temp_node.next  # Move to the next node
                index += 1
            # Insert the node at the specified location
            next_node = temp_node.next
            temp_node.next = new_node
            new_node.next = next_node
    
    def transverse(self):
        if self.head is None:  # Check if the list exists
            print("The list is empty.")
            return
        
        temp_node = self.head  # Start from the head
        while temp_node:
            print(temp_node.value)  # Print the value of the current node
            temp_node = temp_node.next  # Move to the next node
            if temp_node == self.head:  # Stop if we loop back to the head
                break
    
    def search(self, node_value):
        if self.head is None:  # Check if the list exists
            return "The list is empty."
        else:
            temp_node = self.head  # Start from the head
            while temp_node:
                if temp_node.value == node_value:  # Check if the current node matches the search value
                    return temp_node.value
                temp_node = temp_node.next  # Move to the next node
                if temp_node == self.head:  # Stop if we loop back to the head
                    break
            return "Node not found"
            
    def deletion(self, location):
        if self.head is None:  # Check if the list exists
            return "The list is empty."
        
        # Deleting the head node
        if location == 0:
            if self.head == self.tail:  # Only one node in the list
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next  # Update the head to the next node
                self.tail.next = self.head  # Update the tail's next to the new head
        
        # Deleting the tail node
        elif location == 1:
            if self.head == self.tail:  # Only one node in the list
                self.head = None
                self.tail = None
            else:
                temp_node = self.head  # Start from the head
                while temp_node.next != self.tail:  # Traverse to the node before the tail
                    temp_node = temp_node.next
                temp_node.next = self.head  # Update the next pointer to the head
                self.tail = temp_node  # Update the tail to the new last node
        
        # Deleting a node at a specific position
        else:
            temp_node = self.head  # Start from the head
            index = 0  # Initialize index
            while index < location - 1 and temp_node.next != self.head:
                temp_node = temp_node.next  # Move to the next node
                index += 1
            # Deletion only if the node exists
            if temp_node.next != self.head:
                temp_node.next = temp_node.next.next  # Bypass the node to delete
            else:
                return "Invalid location"

# Example usage:
C1 = CircularSLL()
C1.creation(1)  # Creating the list with a single node (1)

C1.insert(1, 0)  # Insert 1 at the beginning
C1.insert(2, 1)  # Insert 2 at the end
C1.insert(3, 2)  # Insert 3 at the end
C1.insert(4, 3)  # Insert 4 at the end

print(C1.search(3))  # Searching for a node with value 3
print(C1.search(5))  # Searching for a non-existent node

# Transversing the list
C1.transverse()

# Using iteration (list comprehension)
print([node.value for node in C1])

C1 = Circular()
C1.Creation(1)

C1.Insertion(0, 0)  # Insert at the beginning
C1.Insertion(2, 1)  # Insert at the end
C1.Insertion(3, 2)  # Insert at index 2
C1.Insertion(4, 3)  # Insert at index 3
C1.Insertion(5, 1)  # Insert at the end

print([node.value for node in C1])
