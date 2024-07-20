#trees
class Treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
         
    def add_child(self,child):
       child.parent=self #child as object having a property of parent
       self.children.append(child)

    def get_level(self):
       level=0
       p=self.parent
       while p:
          level+=1
          p=p.parent

        
       return level


    def print_tree(self):
        spaces=" " * self.get_level()*10
        print(spaces+self.data)#prefix is the no. spaces
        #print(self.data)
        if len(self.children)>0:
         for child in self.children:
            child.print_tree()



def bulid_product_tree():
      root=Treenode("Electronics")
      laptop=Treenode("laptop")
      laptop.add_child(Treenode("l"))
      laptop.add_child(Treenode("top"))


      
      
      cellphone=Treenode("Cell phone")
      cellphone.add_child(Treenode("iphone"))
      cellphone.add_child(Treenode("ip"))
      cellphone.add_child(Treenode("hone"))

      tv=Treenode("tv")
      tv.add_child(Treenode("samsung"))
      tv.add_child(Treenode("LG"))


      

      root.add_child(laptop)
      root.add_child(cellphone)
      root.add_child(tv)

      print(tv.get_level())
      return root



if __name__=="__main__":
 root=bulid_product_tree()
 root.print_tree()
 print(root.get_level())
 pass