class Stack:
    def __init__(self):
        self.list=[];
    def __str__():
        values=self.list.reverse();
        values=[str(x) for x in self.list];
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
customstack=Stack();
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)
customstack.pop()
print(customstack)
