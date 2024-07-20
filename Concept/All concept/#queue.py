#queue
from collections import deque

class Queue:
    def __init__(self):
        self.buffer=deque()#class object called buffer
    
    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
       return self.buffer.pop()

    def is_empty(self):
        if len(self.buffer)==0:
         print("ok")
        
        else:
           print("not empty")
    
    def size(self):
     print(len(self.buffer))
     return
    
    def display(self):
       print(self.buffer)

if __name__=="__main__":
   q=Queue()
   q.enqueue(1)
   q.enqueue(2)
   q.enqueue(3)
   q.enqueue(4)
   q.display()
   q.dequeue()
   q.display()
   q.size()
   q.is_empty()
