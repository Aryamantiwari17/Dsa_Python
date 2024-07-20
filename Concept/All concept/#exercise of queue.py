#exercise of queue
from collections import deque
import time
import threading

class Queue:   
    def __init__(self):
        self.buffer=deque()

    def enque(self,val):
        self.buffer.appendleft(val)
        

    def dam(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            exit
          
        
        else:

         return self.buffer.pop()
    

food_order=Queue()


def placed_order(orders):
    for order in orders:
        print("placing order",order)
        food_order.enque(order)
        time.sleep(0.5)

def recive_order():
    time.sleep(1)
    while True:
     order=food_order.dam()
     print("recive order",order)
     time.sleep(1)

if __name__=="__main__":
    
    orders=["pizza","samosa","pasta","biryani","burger"]
   
    t1 = threading.Thread(target=placed_order, args=(orders,))
    
    t2 = threading.Thread(target=recive_order)

    t1.start()
    t2.start()
    
    t1.join()

    t2.join()
    print("Done!")


                                 