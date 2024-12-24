class Queue:
    def __init__(self):
        self.item=[]
    def __str__(self):
        value = [str(x) for x in self.item]
        return ' '.join(value)
    def isEmpty(self):
        return self.item == []
    def enque(self,value):
        self.item.append(value)
        return "the element is inserted"