#linked list 
class Node:

 def __init__(self,data=None,next=None):
   self.data=data
   self.next=next

class LinkedList:
  def __init__(self):
    self.head=None

  def insert_at_beginig(self,data):
     node=Node(data,self.head)
     self.head=node
    
  def print_list(self):          
    if self.head is None:
     print("Link list is empty") 
     return
    
    itr=self.head
    llstr=" "

    while itr:
     llstr+= str(itr.data)+"--->"
     itr=itr.next
    llstr += "None" 
    print(llstr)
  
  def inseT_at_end(self,data):
    if self.head is None:
       self.head=Node(data,None)
       return
    itr=self.head
    while itr.next:
      itr=itr.next
    itr.next=Node(data,None)

  def insert_values(self,data_list):
      self.head=None
      for data in data_list:
        self.inseT_at_end(data)
     
  def count_ll(self):
    count=0
    itr=self.head
    while itr:
      count+=1
      itr=itr.next  
    return count
    
  
  def remove_at_end(self,index):
    if index<0 or  index>= self.count_ll():
      raise Exception ("invalid Index")
    
    if index==0:
      self.head=self.head.next#point towards next head
      return
    
    count=0
    itr=self.head
    while itr:
      if count==index-1:#comparison
        itr.next=itr.next.next
        break

      itr=itr.next
      count+=1

  def insert_at(self,index,data):
    if index<0 or  index>= self.count_ll():
      raise Exception ("invalid Index")
    
    if index==0:
      self.insert_at_beginig(data)
      #point towards next head
      return
    count=0
    itr=self.head
    while itr:
      if count==index-1:#we are intillazing the previous elment 
         node=Node(data,itr.next)#previous elemnt neext== this element next
         itr.next=node
         break
      itr=itr.next
      count+=1

  def insert_after_value(self,data_after,data_to_insert):
        count=0
        itr=self.head
        while itr:
          if itr.data==data_after:
            node=Node(data_to_insert,itr.next)
            itr.next=node
            break
          itr=itr.next
          count+=1
  def remove_by_value(self,data):
    if self.head is None:
      return
    if self.head.data==data:
      self.head=self.head.next
      return
    count=0
    itr=self.head
    while itr:
      if itr.next.data==data:
        itr.next=itr.next.next
        break
      itr=itr.next
      count+=1
    
      
 
    

if __name__=='__main__':
  #ll.inseT_at_end(178)
  ll=LinkedList()
  ll.insert_values(["banana","orange","grapes","mango"])
  ll.print_list()
  ll.insert_after_value("orange","apple")
  ll.print_list()
  ll.remove_by_value("orange")
  ll.print_list()
 # print("length:",ll.count_ll())
 # ll.remove_at_end(3)
 # ll.insert_at(2,"fig")
 # ll.print_list()
  