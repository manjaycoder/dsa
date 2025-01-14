from linkedlist import LinkedList
def Sum(ll1,ll2):
    n1=ll1.head
    n2=ll2.head
    carry=0
    ll=LinkedList()
    while n1 or n2:
        result=carry
        if n1:
            result+=n1.value
            n1=n1.next
        if n2:
            result+=n2.value
            n2=n2.next
        ll.add(int(result%10))
        carry=result/10
    return ll
ll1=LinkedList()
ll1.add(1)
ll1.add(2)
ll1.add(3)
print(ll1)
ll2=LinkedList()
ll2.add(3)
ll2.add(2)
ll2.add(1)
print(ll2)
print(Sum(ll1,ll2))