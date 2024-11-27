class Node:
    # Node class represents an element in the linked list
    def __init__(self, value=None):
        self.value = value  # Data value of the node
        self.next = None    # Pointer to the next node, initially set to None

class SLinkd_list:
    # Singly Linked List class
    def __init__(self):
        self.head = None  # Head points to the first node in the list
        self.tail = None  # Tail points to the last node in the list

    def __iter__(self):
        # Iterator to traverse the linked list
        node = self.head
        while node:
            yield node  # Yield each node one by one
            node = node.next

    def insert(self, value, location):
        # Insert a new node with given value at the specified location
        newNode = Node(value)  # Create a new node with the given value
        if self.head is None:  # If the list is empty, both head and tail are the new node
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:  # Insert at the beginning (head)
                newNode.next = self.head  # Point new node to current head
                self.head = newNode  # Update head to new node
            elif location == 1:  # Insert at the end (tail)
                self.tail.next = newNode  # Current tail points to new node
                self.tail = newNode  # Update tail to new node
            else:  # Insert at an arbitrary location
                tempNode = self.head
                index = 0
                # Traverse to the node just before the desired location
                while index < location - 1 and tempNode:
                    tempNode = tempNode.next
                    index += 1
                if tempNode:  # If the location is valid (i.e., the node exists)
                    newNode.next = tempNode.next  # Point new node to the next node
                    tempNode.next = newNode  # Link previous node to the new node
                    if newNode.next is None:  # If inserted at the end, update the tail
                        self.tail = newNode

    def transverse(self):
        # Print all values in the linked list
        if self.head is None:
            print("The linked list is empty.")
        else:
            node = self.head
            while node is not None:
                print(node.value, end=" -> ")  # Print node value
                node = node.next
            print("None")  # Indicate the end of the list

    def search(self, nodeValue):
        # Search for a node with a specific value
        if self.head is None:  # Check if the list is empty
            return "The linked list is empty."
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:  # Found the node
                    return node.value
                node = node.next
            return "Item not found."  # Value not found in the list

    def delete(self, location):
        # Delete a node at the specified location
        if self.head is None:
            print('The linked list does not exist or is empty.')
        else:
            if location == 0:  # Deleting the head (first node)
                if self.head == self.tail:  # Only one node in the list
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next  # Update head to the next node
            elif location == 1:  # Deleting the tail (last node)
                if self.head == self.tail:  # Only one node in the list
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    # Traverse to the second-to-last node
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None  # Remove the tail
                    self.tail = node  # Update the tail to the second-to-last node
            else:  # Deleting a node at an arbitrary location
                tempNode = self.head
                index = 0
                while index < location - 1 and tempNode:  # Traverse to the node before the desired location
                    tempNode = tempNode.next
                    index += 1
                if tempNode and tempNode.next:  # If the location is valid and there's a node to delete
                    tempNode.next = tempNode.next.next  # Remove the node by skipping it

# Testing the code
single = SLinkd_list()
single.insert(1, 1)  # Insert 1 at the end
single.insert(2, 1)  # Insert 2 at the end
single.insert(3, 1)  # Insert 3 at the end
single.insert(4, 1)  # Insert 4 at the end
single.insert(5, 1)  # Insert 5 at the end
single.insert(0, 0)  # Insert 0 at the beginning
single.insert(6, 1)  # Insert 6 at the end
 # Delete the second node

# Print all node values in the list
single.delete(2) 
print([node.value for node in single])

# Transverse the list and print all nodes


single.transverse()
# Search for a node with value 6

