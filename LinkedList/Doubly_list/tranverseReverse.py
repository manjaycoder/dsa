class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoublySLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createSLL(self, nodeValue):
        # Create a single node linked list
        node = Node(nodeValue)
        self.head = node
        self.tail = node
        return "Doubly linked list created with node value " + str(nodeValue)

    def insertion(self, value, location):
        newNode = Node(value)
        if self.head is None:
            return "The linked list is empty"
        elif location == 0:  # Insert at the beginning
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        elif location == 1:  # Insert at the end
            newNode.next = None
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        else:  # Insert at a specific location
            tempNode = self.head
            index = 0
            while index < location - 1 and tempNode.next is not None:
                tempNode = tempNode.next
                index += 1
            if tempNode.next is None:  # If location exceeds the list length, insert at the end
                newNode.next = None
                newNode.prev = tempNode
                tempNode.next = newNode
                self.tail = newNode
            else:
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next.prev = newNode
                tempNode.next = newNode

    def traverse(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value, end=" -> ")
                tempNode = tempNode.next
            print("None")

    def traverseReverse(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value, end=" -> ")
                tempNode = tempNode.prev
            print("None")

# Test the Doubly Linked List
D1 = DoublySLL()
print(D1.createSLL(1))
D1.insertion(0, 0)  # Insert at the beginning
D1.insertion(2, 1)  # Insert at the end
D1.insertion(3, 2)  # Insert at a specific location
D1.insertion(4, 10)  # Insert at a location out of bounds (appends to the end)

print("Traverse forward:")
D1.traverse()

print("\nTraverse reverse:")
D1.traverseReverse()

print("\nLinked List Values:", [node.value for node in D1])
