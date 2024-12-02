class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Circular:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head  # Initialize node to the head of the circular list
        while node:
            yield node  # Yield the current node
            if node.next == self.head:  # Check if we have cycled back to the head
                break
            node = node.next

    def creation(self, value):
        node = Node(value)
        node.next = node  # Point the node to itself (circular link)
        self.head = node
        self.tail = node
    def insertion(self,value,location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode=Node(value)
            if location == 0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif location == 1:
                newNode.next=self.tail.next
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode
                tempNode.next=newNode
                tempNode.next=newNode
                nextNode.next=newNode

                



# Create the circular list and add a node
single = Circular()
single.creation(1)
single.insertion(1,0)
single.insertion(2,2)
single.insertion(3,3)
# Iterate through the list and print the values
print([node.value for node in single])  # Iterate over the instance, not the class
