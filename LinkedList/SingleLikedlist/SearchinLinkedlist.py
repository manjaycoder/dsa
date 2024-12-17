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
        if self.head is None:  # If list is empty
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:  # Insert at the beginning
                newNode.next = self.head
                self.head = newNode
            elif location == 1:  # Insert at the end
                self.tail.next = newNode
                self.tail = newNode
            else:  # Insert at an arbitrary location
                tempNode = self.head
                index = 0
                while index < location - 1 and tempNode:  # Traverse to the node before the desired location
                    tempNode = tempNode.next
                    index += 1
                if tempNode:  # If the location is valid
                    newNode.next = tempNode.next
                    tempNode.next = newNode
                    if newNode.next is None:  # Update tail if inserted at the end
                        self.tail = newNode

    def transverse(self):
        if self.head is None:
            print("The linked list is empty.")
        else:
            node = self.head
            while node is not None:
                print(node.value, end=" -> ")
                node = node.next
            print("None")  # End of list
    def search(self,nodeValue):
        if self.head is Node:
            return "the linked list is not found"
        else:
            node=self.head
            while node is not None:
                if node.value==nodeValue:
                    return node.value
                node=node.next
            return "the item is not found"
                


# Testing the code
single = SLinkd_list()
single.insert(1, 1)
single.insert(2, 1)
single.insert(3, 1)
single.insert(4, 1)
single.insert(5, 1)
single.insert(0, 0)  # Insert at the beginning
single.insert(6, 1)  # Insert at the end

# Print all node values in the list
print([node.value for node in single])

# Transverse the list
single.transverse()
print(single.search(6))