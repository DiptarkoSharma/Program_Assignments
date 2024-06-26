class BinarySearchTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if self.data == data:
            return
        if self.data > data :
            #Assign to left Search tree
            if self.left : #Child exists  in left subtree
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)#Add left child node
        else: #Assign to right search tree
            if self.right : #Child exists  in right subtree
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)#Add left child node
    def in_order_traversal(self):
        #in order traversal
        #First left tree
        # then root node
        #Then right tree
        elements = []
        #Left
        if self.left:
            elements +=self.left.in_order_traversal()
        #Base
        elements.append(self.data)
        #right traversal
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    def search(self,val):

        if self.data == val:
            #Exact match found
            return True
        elif self.data > val:
            #search in left search tree
            if self.left:
                
                return  self.left.search(val)

            else:
                return False #Nothing found
        else:
            #search in left search tree
            if self.right:
                
                return  self.right.search(val)

            else:
                return False #Nothing found
    
    def find_max(self):
        # If there is no right child, the current node is the maximum value.
        if self.right is None:
            return self.data
        # If there is a right child, the maximum value is in the right subtree.
        # Recursively call find_max on the right subtree to find the maximum
        # value.
        return self.right.find_max()

    def find_min(self):
        # The minimum value in a BST is the leftmost node.
        if self.left is None:
            return self.data
        # Recursively go to the left to find the smallest value.
        return self.left.find_min()
    
    def delete(self, val):
        # If the value to be deleted is less than the current node's value,
        # then it lies in the left subtree.
        if val < self.data:
            if self.left:
                # Recursively call delete on the left subtree.
                self.left = self.left.delete(val)
        # If the value to be deleted is greater than the current node's value,
        # then it lies in the right subtree.
        elif val > self.data:
            if self.right:
                # Recursively call delete on the right subtree.
                self.right = self.right.delete(val)
        # If the value is equal to the current node's value, then this is
        #the node to be deleted.
        else:
            # Case 1: Node with no children (leaf node).
            if self.left is None and self.right is None:
                return None
            # Case 2: Node with only one child (right child).
            elif self.left is None:
                return self.right
            # Case 2: Node with only one child (left child).
            elif self.right is None:
                return self.left

            # Case 3: Node with two children.
            # Find the inorder successor (smallest in the right subtree).
            min_val = self.right.find_min()
            # Replace the data of this node with the inorder successor's data.
            self.data = min_val
            # Delete the inorder successor.
            self.right = self.right.delete(min_val)

        return self

#Helper method
def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for itr in range(1,len(elements)):
        root.add_child(elements[itr])
    return root



if __name__ =='__main__':
    elements = [17,5,6,24]
    numbers_tree = build_tree(elements)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(25))
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)

    print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)
    print(country_tree.in_order_traversal())
    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    

                


            
