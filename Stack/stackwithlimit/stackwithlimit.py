class Stack:
    def __init__(self, maxLimit):
        self.maxLimit = maxLimit
        self.list = []
    
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]  # Properly reverse for display
        return "\n".join(values)
    
    def isEmpty(self):
        return self.list == []  # Correctly return True/False
    
    def isFull(self):
        return len(self.list) == self.maxLimit  # Check based on the length of the list
    
    def push(self, value):
        if self.isFull():  # Use the isFull() method for clarity
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element is successfully inserted"
    
    def pop(self):
        if self.isEmpty():  # Check if the stack is empty before popping
            return "The stack is empty"
        return self.list.pop()

# Example usage
customStack = Stack(2)  # Create a stack with a maximum size of 2
print(customStack.push(1))  # Insert 1
print(customStack.push(2))  # Insert 2
print(customStack.push(3))  # Attempt to insert 3 (should fail)
print("\nStack Content:\n", customStack)  # Display stack contents
