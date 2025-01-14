class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SingleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:  # Empty list
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:  # Insert at the beginning
                newNode.next = self.head
                self.head = newNode
            elif location == -1:  # Insert at the end
                self.tail.next = newNode
                self.tail = newNode
            else:  # Insert at a specific location
                tempNode = self.head
                index = 0
                while index < location - 1 and tempNode.next:  # Traverse to the desired position
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if newNode.next is None:  # Update tail if new node is at the end
                    self.tail = newNode

# Testing the SingleList implementation
custom = SingleList()

# Insert nodes into the list
custom.insertSLL(2, 0)   # Insert at the beginning
custom.insertSLL(1, 0)   # Insert at the beginning again
custom.insertSLL(3, -1)  # Insert at the end
custom.insertSLL(1, 2)   # Insert at position 2
custom.insertSLL(4, -1)  # Insert at the end again

# Print the linked list values
print([node.value for node in custom])
