#what is likedlist?
#linked list is a form of a sequental collection and it does not have to be in order. a linked list is made up of independent nodes that may contain any type of data and each node has a reference to the next node in the link
#linked list v/s arrays 
#type of linkedlist single linked list,circular singly linked list,doubled linked list,circular doubley linked list
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class SLinkd_list:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    


singleLinkedlist=SLinkd_list()
print([node.value for node in singleLinkedlist])

