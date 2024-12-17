from linkedlist import LinkedList
#create a function to return n to last node in linkdelist
def nthtoLast(ll,n):
    #initialize the two pointer to travel  to start to end 
    pointer1=ll.head
    pointer2=ll.head
    for i in range(n):
        #it return None if the pointer1 is greater than the length of the linkdelist
        if pointer1 is None:
            return None
        #it move the one step to next
        pointer2=pointer2.next
        #the while is travel until the pointer2 is travel the end of the linkedlist
    while pointer2:
        #two pointer move the last the node but pointer2 is move one step fast than the pointer1
        pointer1=pointer1.next
        pointer2=pointer2.next
        #last the last nth node 
    return pointer1
Custom=LinkedList()
Custom.generate(10,0,9)
print(Custom)
print(nthtoLast(Custom,3))