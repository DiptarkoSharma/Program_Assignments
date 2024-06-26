# A simple Python program to introduce a linked list
class Node():
    # Function to initialize the node object
    def __init__(self):
        self.data = data
        self.next = None ## Initialize
                        # next as null

class LinkedList():
    def __init__(self):
        self.head = None
        
#Let us introduce 3 nodes here

if __name__=='__main__':
    llist = LinkedList()
    if not llist.head:
        llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third

    llist.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | None |     | 2 | None |     | 3 | None |
    +----+------+     +----+------+     +----+------+
    '''
    llist.head.next = second
    second.next = third# Link second node with the third node

    '''
    Now next of second Node refers to third. So all three
    nodes are linked.

    llist.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | o-------->| 2 | o-------->| 3 | null |
    +----+------+     +----+------+     +----+------+
    '''
    
        
    
