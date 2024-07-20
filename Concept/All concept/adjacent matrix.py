#graph adjacency list
 
class Vertex:
    def __init__(self,data):
        self.vertex=data
        self.next=None



class Graph():
    def __init__(self,vertices):
        self.nV=vertices#nv---non -visited
        self.graph_arr=[None]*self.nV
    
    def add_edge(self,src,dest):
        node=Vertex(dest)#1-none
        node.next= self.graph_arr[src]
        self.graph_arr[src]=node

        node=Vertex(src)
        node.next=self.graph_arr[dest]
        self.graph_arr[dest]=node

    
    def print(self):
        for i in range (self.nV):
            print("Adjacency list of vertex ",i,":",end=" ")
            temp=self.graph_arr[i]
            while temp:
                print(temp.vertex," ",end=" ")
                temp=temp.next
        




if __name__=="__main__":
    
      graph=Graph(5)
      graph.add_edge(0,1)
      graph.add_edge(1,2)
      graph.add_edge(1,3)
      graph.add_edge(3,0)
      graph.add_edge(2,3)

      graph.print()


