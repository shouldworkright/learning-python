
# Example of a linked list implementation in Python.
# Author: Dan Mello
# Version: 1.0
# Date: 2019-18-12 

# Define a node class.
class Node:

    # Initializes a node.
    def __init__(self, value):
        self.value = value  # A node's value.
        self.next = None    # A pointer to the next node.

    # Returns a node's value.
    def get_value(self):
        return self.value

# Define a linked Llist class.
class LinkedList:

    # Initializes a linked list.
    def __init__(self):
        self.head = None

    # Prints all nodes within a linked list.
    def printList(self):
        
        currentNode = self.head
        
        while (currentNode):
            print(currentNode.value)
            currentNode = currentNode.next

# Define main.
def main():

    # Initialize nodes.
    first = Node(1)
    second = Node(2)
    third = Node(3)

    # Initialize linked list.
    linkedList = LinkedList()

    # Link each node.
    linkedList.head = first
    first.next = second
    second.next = third

    # Print the linked list.
    linkedList.printList()

# Driver code.
if __name__ == "__main__":
    main()