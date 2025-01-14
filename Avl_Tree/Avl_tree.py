from queue import Queue  # Using standard Python queue module

class AVL:
    def __init__(self, data):
        self.data = data  # Node value
        self.leftChild = None  # Left child node
        self.rightChild = None  # Right child node
        self.height = 1  # Height of the node for balancing purposes

def pre_order(rootNode):
    if not rootNode:
        return
    print(rootNode.data)  # Print root data
    pre_order(rootNode.leftChild)  # Traverse left subtree
    pre_order(rootNode.rightChild)  # Traverse right subtree

def in_order(rootNode):
    if not rootNode:
        return
    in_order(rootNode.leftChild)  # Traverse left subtree
    print(rootNode.data)  # Print root data
    in_order(rootNode.rightChild)  # Traverse right subtree

def post_order(rootNode):
    if not rootNode:
        return
    post_order(rootNode.leftChild)  # Traverse left subtree
    post_order(rootNode.rightChild)  # Traverse right subtree
    print(rootNode.data)  # Print root data

def level_order(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()  # Create a queue
        customQueue.put(rootNode)  # Enqueue the root node
        while not customQueue.empty():
            root = customQueue.get()  # Dequeue the front node
            print(root.data)  # Print node data
            if root.leftChild is not None:
                customQueue.put(root.leftChild)  # Enqueue left child
            if root.rightChild is not None:
                customQueue.put(root.rightChild)  # Enqueue right child

def search(rootNode, nodeValue):
    if not rootNode:
        print("The value is not found")
        return
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        search(rootNode.leftChild, nodeValue)  # Search in the left subtree
    else:
        search(rootNode.rightChild, nodeValue)  # Search in the right subtree

def get_height(rootNode):
    if not rootNode:
        return 0  # Return 0 for null nodes
    return rootNode.height

def right_rotation(disbalancedNode):
    newRoot = disbalancedNode.leftChild  # New root will be the left child
    disbalancedNode.leftChild = newRoot.rightChild  # Update left child
    newRoot.rightChild = disbalancedNode  # Update new root's right child

    # Update heights
    disbalancedNode.height = 1 + max(get_height(disbalancedNode.leftChild), get_height(disbalancedNode.rightChild))
    newRoot.height = 1 + max(get_height(newRoot.leftChild), get_height(newRoot.rightChild))

    return newRoot  # Return the new root

def left_rotation(disbalancedNode):
    newRoot = disbalancedNode.rightChild  # New root will be the right child
    disbalancedNode.rightChild = newRoot.leftChild  # Update right child
    newRoot.leftChild = disbalancedNode  # Update new root's left child

    # Update heights
    disbalancedNode.height = 1 + max(get_height(disbalancedNode.leftChild), get_height(disbalancedNode.rightChild))
    newRoot.height = 1 + max(get_height(newRoot.leftChild), get_height(newRoot.rightChild))

    return newRoot  # Return the new root

def get_balance(rootNode):
    if not rootNode:
        return 0  # Return 0 for null nodes
    return get_height(rootNode.leftChild) - get_height(rootNode.rightChild)  # Calculate balance factor

def insert_node(rootNode, nodeValue):
    if not rootNode:
        return AVL(nodeValue)  # Create a new node if root is null
    if nodeValue < rootNode.data:
        rootNode.leftChild = insert_node(rootNode.leftChild, nodeValue)  # Insert in the left subtree
    else:
        rootNode.rightChild = insert_node(rootNode.rightChild, nodeValue)  # Insert in the right subtree

    # Update height of the current node
    rootNode.height = 1 + max(get_height(rootNode.leftChild), get_height(rootNode.rightChild))

    # Get balance factor to check if the node is unbalanced
    balance = get_balance(rootNode)

    # Perform rotations to balance the tree
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return right_rotation(rootNode)  # Right rotation

    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = left_rotation(rootNode.leftChild)  # Left rotation on left child
        return right_rotation(rootNode)  # Right rotation

    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return left_rotation(rootNode)  # Left rotation

    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = right_rotation(rootNode.rightChild)  # Right rotation on right child
        return left_rotation(rootNode)  # Left rotation

    return rootNode  # Return the (possibly updated) root node

# Create AVL tree and insert nodes
newAVL = AVL(5)
newAVL = insert_node(newAVL, 10)
newAVL = insert_node(newAVL, 20)
newAVL = insert_node(newAVL, 30)
newAVL = insert_node(newAVL, 40)

# Perform level order traversal
level_order(newAVL)
