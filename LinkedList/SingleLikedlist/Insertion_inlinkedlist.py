class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkd_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):
        newNode = Node(value)

        if self.head is None:  # If the list is empty
            self.head = newNode
            self.tail = newNode
        elif location == 0:  # Insert at the beginning
            newNode.next = self.head
            self.head = newNode
        else:  # Insert at the end (location >= 1)
            if self.tail is not None:
                self.tail.next = newNode
                self.tail = newNode

# Create the linked list and insert values
single = SLinkd_list()
single.insert(1, 1)
single.insert(2, 1)
single.insert(3, 1)
single.insert(4, 1)
single.insert(5, 1)
single.insert(0, 0)
single.insert(6, 1)

# Print all the values in the linked list
print([node.value for node in single])
