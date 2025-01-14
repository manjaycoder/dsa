class Queue:
    def __init__(self, maxSize):
        # Initialize the queue with a fixed size
        self.items = maxSize * [None]  # Pre-allocate the list with None values
        self.maxSize = maxSize  # Set the maximum size of the queue
        self.top = -1  # Pointer to the most recently added item
        self.start = -1  # Pointer to the front of the queue

    def __str__(self):
        # Convert queue items to a string representation
        values = [str(x) for x in self.items]  # Convert each item to string
        return ' '.join(values)  # Join all strings with a space

    def isFull(self):
        # Check if the queue is full
        if self.top + 1 == self.start:  # Case when queue is full in circular mode
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:  # Queue wraps around and reaches the start
            return True
        else:
            return False

    def isEmpty(self):
        # Check if the queue is empty
        if self.top == -1:  # Queue is empty when top is -1
            return True
        else:
            return False

    def enque(self, value):
        """
        Add an element to the queue.
        """
        if self.isFull():  # Check if the queue is full
            return "The queue is fully filled"
        else:
            # Handle circular nature of the queue
            if self.top + 1 == self.maxSize:  # If end of array is reached
                self.top = 0  # Wrap around to the beginning
            else:
                self.top += 1  # Increment the top pointer

            # If the queue was empty, update the start pointer
            if self.start == -1:
                self.start = 0

            self.items[self.top] = value  # Insert the value at the top position
            return "Inserted"

    def dequeue(self):
        """
        Remove and return the front element of the queue.
        """
        if self.isEmpty():  # Check if the queue is empty
            return "Not any element"
        else:
            # Retrieve the first element
            firstElement = self.items[self.start]
            start = self.start  # Store the current start position

            # Update pointers based on the current state
            if self.start == self.top:  # If only one element was in the queue
                self.start = -1  # Reset to empty state
                self.top = -1
            elif self.start + 1 == self.maxSize:  # If start reaches end of array
                self.start = 0  # Wrap around to the beginning
            else:
                self.start += 1  # Move the start pointer forward

            self.items[start] = None  # Clear the dequeued position
            return firstElement  # Return the dequeued element

    def peek(self):
        """
        View the front element of the queue without removing it.
        """
        if self.isEmpty():  # Check if the queue is empty
            return "There is no any element"
        else:
            return self.items[self.start]  # Return the front element

# Example usage of the queue
custom = Queue(5)  # Create a queue with a maximum size of 5
custom.enque(1)  # Insert 1 into the queue
custom.enque(2)  # Insert 2 into the queue
custom.enque(3)  # Insert 3 into the queue
custom.enque(4)  # Insert 4 into the queue

# Remove the front element and print it
print(custom.dequeue())  # Output: 1

# Print the current state of the queue
print(custom)  # Output: None 2 3 4 None
