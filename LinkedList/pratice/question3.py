from linkedlist import LinkedList

def partition(ll, x):
    # Initialize pointers for traversing the linked list
    curr = ll.head
    
    # Temporary pointers to build two sublists: one for nodes with values < x, and one for nodes with values >= x
    less_head = less_tail = None  # These will point to the head and tail of the "less than x" list
    greater_head = greater_tail = None  # These will point to the head and tail of the "greater than or equal to x" list
    
    # Traverse the original linked list
    while curr:
        # Store the next node to avoid losing the rest of the list
        next_node = curr.next
        # Disconnect the current node from the list to prevent cycles (for clarity)
        curr.next = None
        
        # If the current node's value is less than x, add it to the "less" list
        if curr.value < x:
            if less_head is None:
                # If the "less" list is empty, initialize it with the current node
                less_head = less_tail = curr
            else:
                # Otherwise, add the current node to the end of the "less" list
                less_tail.next = curr
                less_tail = curr
        else:
            # If the current node's value is greater than or equal to x, add it to the "greater" list
            if greater_head is None:
                # If the "greater" list is empty, initialize it with the current node
                greater_head = greater_tail = curr
            else:
                # Otherwise, add the current node to the end of the "greater" list
                greater_tail.next = curr
                greater_tail = curr
        
        # Move to the next node in the original list
        curr = next_node
    
    # After partitioning, combine the "less" and "greater" lists:
    if less_tail:
        # If the "less" list has nodes, connect its tail to the "greater" list
        less_tail.next = greater_head
        # The head of the "less" list is the head of the new list
        ll.head = less_head
    else:
        # If the "less" list is empty, the head of the new list should be the head of the "greater" list
        ll.head = greater_head
    
    # The tail of the final list should be the tail of the "greater" list, or the "less" list if no greater nodes
    if greater_tail:
        ll.tail = greater_tail
    else:
        # If the "greater" list is empty, the tail of the final list should be the tail of the "less" list
        ll.tail = less_tail

# Testing the function
custom = LinkedList()
custom.generate(10, 0, 9)  # Generate a linked list with random values between 0 and 9
print("Before partition:", custom)
partition(custom, 5)  # Partition the list around the value 5
print("After partition:", custom)
