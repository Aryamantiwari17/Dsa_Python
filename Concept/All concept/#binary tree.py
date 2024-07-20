#binary tree
#every node has at most 2 child nodes
#BST-Binary Search Tree
class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data== self.data:
         return
        
        if data<self.data:
           #add data in left subtree
           if self.left:
              self.left.add_child(data)
              pass
           else:
              self.left=BinarySearchTree(data)
        else:
           if self.right:
              self.right.add_child(data)
           else:
              self.right= BinarySearchTree(data)


    def in_order_travs(self):
       elements=[]
       #visit left tree
       if self.left:
          elements+= self.left.in_order_travs()

       elements.append(self.data)
       
       if self.right:
          elements+=self.right.in_order_travs()

       return elements
    
    def pre_order_traversal(self):
       elements=[self.data]
     

       if self.left:
          elements+= self.left.pre_order_traversal()

       if self.right:
          elements+=self.right.pre_order_traversal()

       return elements
    
    def post_order_traversal(self):
       
       elements=[]

       if self.left:
          elements+= self.left.post_order_traversal()


       if self.right:
          elements+=self.right.post_order_traversal()

       elements.append(self.data)

       return elements


   
    
    def search (self,val):
       if self.data==val:
          return True
       
       if val<self.data:
          #val might be in a left subtree
          if self.left:
             return self.left.search(val)#search is 
             
          else:
             return False

       if val>self.data:
          #val might be right subtree
          if self.right:
              return self.right.search(val)
          else:
             return False
          
        
          

def bulid_tree(elements):
    root=BinarySearchTree(elements[0])#assigning the root node
    for i in range(1,len(elements)):
       root.add_child(elements[i])


    return root
       

    

if __name__=="__main__":
      numbers=[17,4,1,20,9,23,18,34,18,4 ]#it sorted the elements and 
      numbers_tree=bulid_tree(numbers)
      print(numbers_tree.pre_order_traversal())
      print(numbers_tree.post_order_traversal())
      print(numbers_tree.in_order_travs())
      
      max=((numbers_tree.in_order_travs())[-1])
      print("max value",max)

      min=((numbers_tree.in_order_travs())[0])
      print("min value:",min)
      
      x=(numbers_tree.in_order_travs())
      y=sum(x)
      print("sum of all elements",y)

     
      print(numbers_tree.search(1))






    

       



        

       
       
              
              
              
              

