from linkedlist import LinkedList
def dulicate(ll):
    if ll.head is None:
        return "the linked list is None exist"
    else:
        CurrNode=ll.head
        visited=set([CurrNode.value])
        while CurrNode.next:
            if CurrNode.next.value in visited:
                CurrNode.next=CurrNode.next.next
            else:
                visited.add(CurrNode.next.value)
                CurrNode=CurrNode.next
        return ll
Custom=LinkedList()
Custom.generate(10,0,9)
print(Custom)
dulicate(Custom)
print(Custom)
