from linkedlist import LinkedList
def intersection(ll1,ll2):
    if ll1.tail is not ll2.tail:
        return False
    len1=len(ll1)
    len2=len(ll2)
    shorter=ll1 if len1 < len2 else ll2
    longer=ll2 if len1> len2 else ll1
    
