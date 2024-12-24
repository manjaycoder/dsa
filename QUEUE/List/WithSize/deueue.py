class Queue:
    def __init__(self,maxSize):
        self.items=maxSize * [None]
        self.maxSize=maxSize
        self.top=-1
        self.start=-1
    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)
    def isFull(self):
        if self.top+1==self.start:
            return True
        elif self.start == 0 and self.top+1 == self.maxSize:
            return True
        else:
            return False
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def enque(self,value):
        def enque(self, value):
            """
            Enqueues a value into the queue.

            This method inserts a value into the queue if the queue is not full. 
            It handles the circular nature of the queue by wrapping around when 
            the end of the queue is reached.

            Parameters:
            value: The value to be inserted into the queue.

            Returns:
            str: A message indicating whether the value was successfully inserted 
                 or if the queue is full.

            Steps:
            1. Check if the queue is full using the isFull() method.
            2. If the queue is full, return a message indicating that the queue is full.
            3. If the queue is not full:
                a. Check if the next position is at the end of the queue.
                b. If it is, wrap around to the beginning of the queue.
                c. Otherwise, increment the top pointer.
                d. If the start pointer is -1 (indicating the queue was empty), set it to 0.
            4. Insert the value at the top position.
            5. Return a message indicating that the value was successfully inserted.
            """
        if self.isFull():
            return "the queue is fully filled"
        else:
            if self.top+1 == self.maxSize:
                self.top=0
            else:
                self.top += 1
                if self.start==-1:
                    self.start=0
            self.items[self.top]=value
            return "inserted"
    def dequeue(self):
        if self.isEmpty():
            return "not any element"
        else:
            firstElement=self.items[self.start]
            start=self.start
            if self.start == self.top:
                self.start=-1
                self.top=-1
            elif self.start+1==self.maxSize:
                self.start=0
            else:
                self.start+=1
            self.items[start]=None
            return firstElement
custom=Queue(5)
custom.enque(1)
custom.enque(2)
custom.enque(3)
custom.enque(4)
print(custom.dequeue())
print(custom)