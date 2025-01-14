class Stack:
    def __init__(self):
        self.list=[]
    def __str__(self):
        if self.list is None:
            return "the stack is empty"
        else:
            values=self.list.reverse()
            values=[str(x) for x in self.list ] 
            return "/n".join(values)