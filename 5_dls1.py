from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.visited=set()
        self.path=list()
    def addedge(self,u,v):
        self.graph[u].append(v)
    def DLS(self,src,target,maxDepth):
        self.path.append(src)
        if(src==target):
            return True
        if(maxDepth<=0):
            return
        self.visited.add(src)
        for i in self.graph[src]:
            if i not in self.visited:
                if(self.DLS(i,target,maxDepth-1)):
                    return True
                self.path.remove(i)
        return False
g=Graph()
e=int(input("Enter the number of edges: "))
print("Enter the edges: ")
for i in range(e):
    a,b=map(int,(input().split()))
    g.addedge(a,b)
target=int(input("Enter target node: "))
maxDepth=int(input("Enter maximun depth: "))
src=int(input("Enter source node: "))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
if g.DLS(src,target,maxDepth)==True:
   print("Target is reachable from source wirhin max depth")
   print(g.path)
else:
   print("Target is NOT rechable from source within max depth")