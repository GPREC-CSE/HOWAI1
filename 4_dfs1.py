graph={}
visted=set()
def addedge(x,y):
    if x not in graph.keys():
        graph[x]=[y]
    else:
        graph[x].append(y)
    if y not in graph.keys():
        graph[y]=[x]
    else:
        graph[y].append(x)
def dfs(visted,graph,start):
    if start not in visted:
        print(start,end=" ")
        visted.add(start)
        for i in graph[start]:
            dfs(visted,graph,i)
addedge(0,1)
addedge(0, 2)
addedge(1, 2)
addedge(2, 0)
addedge(2, 3)
addedge(3, 3)
 
dfs(visted,graph,2)