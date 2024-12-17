class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        if node:
            while True:
                yield node
                node = node.next
                if node == self.head:  # Stop if we have looped back to the head
                    break
    
    def creation(self, node_value):
        new_node = Node(node_value)
        self.head = new_node
        self.tail = new_node
        self.tail.next = self.head  # Circular reference
    
    def insert(self, value, location):
        if self.head is None:
            return "The list is empty, cannot insert."
        
        new_node = Node(value)
        
        # Insert at the beginning (location 0)
        if location == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head  # Maintain circular linkage
            
        # Insert at the end (location 1)
        elif location == 1:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            
        else:
            temp_node = self.head
            index = 0
            # Traverse to the correct position
            while index < location - 1 and temp_node.next != self.head:
                temp_node = temp_node.next
                index += 1
            
            # Insert the node at the specified location
            next_node = temp_node.next
            temp_node.next = new_node
            new_node.next = next_node
    
    def transverse(self):
        if self.head is None:
            print("The list is empty.")
            return
        
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop at the head to avoid infinite loop
                break
    
    def search(self, nodeValue):
        if self.head is None:
            return "The list is empty."
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == nodeValue:
                    return temp_node.value
                temp_node = temp_node.next
                if temp_node == self.head:
                    break
            return "Node not found"
            
    def deletion(self, location):
        if self.head is None:
            return "The list is empty."
        
        # Deleting the head node
        if location == 0:
            if self.head == self.tail:  # Only one node
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head  # Update tail next to head
        
        # Deleting the tail node
        elif location == 1:
            if self.head == self.tail:  # Only one node
                self.head = None
                self.tail = None
            else:
                temp_node = self.head
                while temp_node.next != self.tail:
                    temp_node = temp_node.next
                temp_node.next = self.head
                self.tail = temp_node
        
        # Deleting a node at a specific position
        else:
            temp_node = self.head
            index = 0
            while index < location - 1 and temp_node.next != self.head:
                temp_node = temp_node.next
                index += 1
            
            # Deletion only if the node exists
            if temp_node.next != self.head:
                temp_node.next = temp_node.next.next
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
