from linkedlist import LinkedList

def remove_duplicate(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])  # Keep track of visited node values
        while currentNode.next:
            if currentNode.next.value in visited:
                # Skip the duplicate node
                currentNode.next = currentNode.next.next
            else:
                # Add the value to the visited set and move forward
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
    return ll  # Ensure to return the linked list after removing duplicates

# Test the function
C1 = LinkedList()
C1.generate(10, 1, 9)  # Generates a linked list with 10 random values between 1 and 9
print("Original Linked List:")
print(C1)

remove_duplicate(C1)

print("Linked List After Removing Duplicates:")
print(C1)
