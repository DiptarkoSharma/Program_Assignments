class Node():
    '''
       A class representing a node in a singly linked list.
        Attributes:
        -----------
        data : Any
            The data stored in the node.
        next : Node or None
            The reference to the next node in the list.
     '''
    
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList():
    ''' 
    
    A class for creating and manipulating a singly linked list.

    Methods:
    --------
    __init__():
        Initializes the linked list with an empty head.
        
    insert_at_beginning(data):
        Inserts a new node at the beginning of the list.
        
    insert_at_end(data):
        Inserts a new node at the end of the list.
        
    print():
        Prints all the elements of the linked list.
        
    insert_values(data_list):
        Inserts multiple values from a list into the linked list.
        
    get_length():
        Returns the length of the linked list.
        
    remove_at(index):
        Removes a node at a specified index.
        
    insert_at(data, index):
        Inserts a node at a specified index.
    
    '''
    def __init__(self):
        self.head = None
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_at_end(self,data):
        """
            Insert a new node at the end of the list.

            Parameters:
            -----------
            data : Any
            The data to insert at the end of the list.
        """
        if self.head is None:
            self.head = Node(data,None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data,None)
    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        llstr=''
        itr = self.head
        while itr:
            llstr+=str(itr.data)+'---->'if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
    def insert_values(self,data_list):
        for itr in data_list:
            self.insert_at_end(itr)
    def get_length(self):
        if self.head is None:
            cnt=0
            print(f'Length of the list is {cnt}')
            return cnt
        else:
            cnt = 1
            itr = self.head
        while itr.next is not None:
            cnt+=1
            itr = itr.next
        print(f'Length of the list is {cnt}')
        return cnt
    def remove_at(self,index):
        try:

            if index <0 or index >= self.get_length():
                raise Exception('Invalid Index')
            if index ==0:
                self.head = self.head.next
            if self.get_length()==0:
                raise Exception('Empty Linked List.')
            else:
                cnt = 0
                itr = self.head
                while itr.next is not None:
                    if cnt == index-1:
                        itr.next = itr.next.next
                        break
                    cnt+=1
                    itr =itr.next

        except Exception as e:
            print(f'{e}')
    
    def insert_at(self,data,index):
        try:
            if index <0 or index >= self.get_length():
                raise Exception('Invalid Index')
            if self.get_length()==0:
                raise Exception('Empty Linked List.')
            if index ==0:
                self.insert_at_begining(data)
                return
            else:
                cnt = 0
                itr = self.head
                while itr.next is not None:
                    if cnt == index-1:
                        n1 = Node(data,itr.next)
                        itr.next = n1
                        break
                    cnt+=1
                    itr =itr.next
                return

        except Exception as e:
            print(f'{e}')
            return

class Double_Node():
    '''
       A class representing a node in a doubly  linked list.
        Attributes:
        -----------
        data : Any
            The data stored in the node.
        prev: The reference to a previous node.
        next : Node or None
            The reference to the next node in the list.
     '''
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.prev = prev
        self.next = next
'''
    Class  to control a doubly linked list
'''
class Double_Linked_List():
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self,data):
        self.head = Double_Node(data,None,None)
         
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, itr, None)
    
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr
    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        llstr=''
        itr = self.head
        while itr:
            llstr+=str(itr.data)+'---->'if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
    def insert_values(self,data_list):
        for itr in data_list:
            self.insert_at_end(itr)
    def get_length(self):
        if self.head is None:
            cnt=0
            print(f'Length of the list is {cnt}')
            return cnt
        else:
            cnt = 1
            itr = self.head
        while itr.next is not None:
            cnt+=1
            itr = itr.next
        print(f'Length of the list is {cnt}')
        return cnt
    def insert_at(self,data,index):
        try:
            if index <0 or index >= self.get_length():
                raise Exception('Invalid Index')
            if self.get_length()==0:
                raise Exception('Empty Linked List.')
            if index ==0:
                self.insert_at_begining(data)
                return
            else:
                cnt = 0
                itr = self.head
                while itr.next is not None:
                    if cnt == index-1:
                        n1 = Double_Node(data,itr.next,itr)
                        itr.next = n1
                        break
                    cnt+=1
                    itr =itr.next
                return

        except Exception as e:
            print(f'{e}')
            return
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)
if __name__=='__main__':
    ll = LinkedList()
    ll.insert_at_begining(7)
    #ll.insert_at_begining(5)
    #ll.insert_at_end(9)
    #ll.insert_values([9,10,11])
    #ll.print()
    #ll.get_length()
    #ll.remove_at(2)
    #ll.print()
    #ll.insert_at(5,0)
    #ll.print()
    #dll = Double_Linked_List()
    #dll.insert_at_begining(5)
    #dll.print()
    #dll.insert_at_end([3,2,4])
    #dll.print()
    #dll.insert_values([3,1,2])
    #dll.print()
    #dll.insert_at('Mango',2)
    #dll.print()
        
