#Creating stacks using Deque
from collections import deque

class Stack():
    def __init__(self):
        self.stack = deque()
    
    def push_one(self,data):
         self.stack.append(data)
        
    def pop_one(self):        
        return self.stack.pop()
        print(f'Stack after one pop is {self.stack}')
    def peek(self):
        return self.stack[-1]
    def peek_at(self,index):
        try:

            if index >= self.size():
                raise Exception('Invalid Index')
            else:
                return self.stack[index]
        except Exception as e:
            print(e)
            return
        return self.stack[-1]
    def is_empty(self):
        return self.stack == None

    def size(self):
        return len(self.stack)

if __name__== '__main__':
    stack = Stack()
    stack.push_one('Mango')
    stack.push_one('Orange')
    stack.push_one('Pineapple')
    stack.push_one('Apple')
    stack.pop_one()
    stack.pop_one()
    print(stack.peek())
    print(stack.size())
