#questions
#doubly link list

class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class Dll:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert_at_begin(self,data):
        node=Node(data,self.head,self.tail)
        if self.head is None:
            self.head=self.tail=node
            self.head.prev=None
            self.tail.next=None
        else:
            self.tail.next=node#newnode will be added after tail such that tail next point to newNode
            node.prev=self.tail#newnode previous will point to tail
            self.tail=node#newNode will become new tail    
            self.tail.next=None#as it is last node it point to none
            
    def  display(self):
        current=self.head
        if(self.head==None):
            print("list empty")
       
        print("print the doubly link list")
        while(current!=None):
            print(current.data,end=" --->")
            current=current.next



dlist=Dll()
dlist.insert_at_begin(10)
dlist.insert_at_begin(20)
dlist.insert_at_begin(30)
dlist.display()




        

        