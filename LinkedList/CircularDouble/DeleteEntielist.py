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
            return "The linked list is empty"
        else:
            newNode = Node(value)
            if location == 0:  # Insert at the beginning
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:  # Insert at the end
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
                self.head.prev = newNode
            else:  # Insert at a specific location
                tempNode = self.head
                index = 0
                while index < location - 1 and tempNode.next != self.head:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next.prev = newNode
                tempNode.next = newNode
        return "The node has been successfully inserted"

    def traverse(self):
        # Traverse and print all the elements in the list
        if self.head is None:
            print("The linked list is empty")
        else:
            tempNode = self.head
            while True:
                print(tempNode.value, end=" -> ")
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
            print("(Back to Head)")

    def traverseReverse(self):
        # Traverse the list in reverse order
        if self.head is None:
            print("The linked list is empty")
        else:
            tempNode = self.tail
            while True:
                print(tempNode.value, end=" -> ")
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev
            print("(Back to Tail)")

    def Searching(self, value):
        # Search for a node with the given value
        if self.head is None:
            return "The linked list is empty"
        else:
            tempNode = self.head
            while True:
                if tempNode.value == value:
                    return f"Value {value} found in the list"
                if tempNode == self.tail:
                    return f"Value {value} not found in the list"
                tempNode = tempNode.next

    def delete(self, location):
        # Delete a node from the list
        if self.head is None:
            print("The linked list is empty")
        else:
            if location == 0:  # Delete from the beginning
                if self.head == self.tail:  # Only one node
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:  # Delete from the end
                if self.head == self.tail:  # Only one node
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:  # Delete at a specific location
                tempNode = self.head
                index = 0
                while index < location - 1 and tempNode.next != self.head:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode

    def deleteEntire(self):
        # Method to delete the entire circular doubly linked list
        if self.head is None:
            print("The linked list is empty")
        else:
            self.tail.next = None  # Break the circular link
            tempNode = self.head
            while tempNode:
                tempNode.prev = None  # Remove the link to the previous node
                tempNode = tempNode.next  # Move to the next node
            self.head = None  # Clear the head pointer
            self.tail = None  # Clear the tail pointer
            return "The linked list is successfully deleted completely"


# Example usage
custom = CircularDoubly()
print(custom.Creation(9))  # Create the list
print(custom.Insertion(5, 0))  # Insert at the beginning
print(custom.Insertion(15, 1))  # Insert at the end
print(custom.Insertion(7, 1))  # Insert in the middle
custom.traverse()  # Print the list
custom.traverseReverse()  # Print the list in reverse
print(custom.Searching(7))  # Search for a value
custom.delete(1)  # Delete the node at the end
custom.traverse()  # Print the updated list
print(custom.deleteEntire())  # Delete the entire list
