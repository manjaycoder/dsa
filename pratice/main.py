class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Single:
    def __init__(self):
        self.head = None
        self.tail = None

    # Define an iterator to traverse the list
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
        elif location == 0:  # Insert at the head
            newNode.next = self.head
            self.head = newNode
        else:  # Insert at the tail (end)
            tempNode=self.head
            index=0
            while index < location -1 and tempNode:
                tempNode=tempNode.next
                index+=1
            if tempNode:
                newNode.next=tempNode.next
                tempNode.next=newNode
                if newNode.next is None:
                    self.tail=newNode
def transverse(self):
    if self.head is None:
        print("the linked list is empty")
    else:
        node=self.head
        while node is not None:
            print(node.value,end='->')
            node=node.next
        print("None")

