class Stack:
    def __init__(self):
        self.list=[];
    def __str__(self):
        values=self.list.reverse();
        values=[str(x) for x in self.list ] ;
        return "\n".join(values);
    def isEmpty(self):
        if self.list == []:
            return True;
        else:
            False;
    def push(self,values):
        self.list.append(values)
        return "the element is successfully inserted"
    def pop(self):
        if self.isEmpty():
            return "this stack is empty"
        else:
            return self.list.pop()
    def peek(self):
        if self.isEmpty():
            return "the element is successfully inserted"
        else:
            return self.list[len(self.list)-1]
    def delete(self):
        self.list=None
        return "the stack is successfull is empty"
customstack=Stack();
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)
print(customstack.delete())


