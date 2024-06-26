#Creating Queues using Deque
from collections import deque
class Queue():
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self,data):
         self.queue.appendleft(data)
        
    def dequeue(self):        
        return self.queue.pop()
        #print(f'Stack after one pop is {self.stack}')
    def peek(self):
        return self.queue[-1]
    def peek_at(self,index):
        try:

            if index >= self.size():
                raise Exception('Invalid Index')
            else:
                return self.queue[index]
        except Exception as e:
            print(e)
            return
        return self.stack[-1]
    def is_empty(self):
        return self.queue == None

    def size(self):
        return len(self.queue)

if __name__ =="__main__":
    pq = Queue()
    pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
    pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})
print(pq.size())
print(pq.dequeue())