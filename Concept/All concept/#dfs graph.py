#dfs graph and bfs graph
graph={#ADJACENT NODES
'A':['B','C','D'] ,#ALREADY COVERED A TO C
'B':['E'],
'C':['E'],
'D':[],
'E':[]

}

visited=set()#Sets are used to store multiple items in a single variable.



def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)#add the root node

        for neighbour in  graph[root]:
            dfs(visited,graph,neighbour)


dfs(visited,graph,'A')



             




