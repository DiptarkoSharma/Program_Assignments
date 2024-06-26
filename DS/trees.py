class TreeNode():
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
  
    def get_level(self):
        level = 0
        p = self.parent
       
        while p:
            level+=1
            p = p.parent
        return level
    
    def print_tree(self):
        level = self.get_level()
        spaces = ' '*(level*3)
        prefix = spaces + "|__" if self.parent else ""
        print(prefix+self.data)
        children = self.children
        if children:
            for child in children:
                child.print_tree()


def build_product_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptops')
    
    mac_book = TreeNode('MacBook') 
    laptop.add_child(mac_book)
    laptop.add_child(TreeNode('ThinkPad'))
    

    cellphones = TreeNode('Cell Phones')
    root.add_child(cellphones)
    
    cellphones.add_child(TreeNode('iPhones'))
    cellphones.add_child(TreeNode('Google Pixel'))

    root.add_child(laptop)
    root.add_child(cellphones)
    print(f'Laptop:{laptop.get_level()}')
    print(f'Macbook: {mac_book.get_level()}')

    print(root.print_tree())
    print(laptop.print_tree())

    return root

if __name__ == '__main__':
    root = build_product_tree()
    #print(root.print_tree())
    #print(root.get_level())
    


