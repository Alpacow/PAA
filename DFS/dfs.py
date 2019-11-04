from collections import defaultdict 
   
#This class represents a directed graph  
# using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        #No. of vertices 
        self.V= vertices  
          
        # default dictionary to store graph 
        self.graph = defaultdict(list)  
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    '''A recursive function to print all paths from 'u' to 'd'. 
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''
  
  
                      
                    self.printAllPathsUtil(i, d, visited, path) 
                if visited[i]==False: 
            # If current vertex is not destination 
            #Recur for all the vertices adjacent to this vertex 
            for i in self.graph[u]: 
            print path 
        # If current vertex is same as destination, then print 
        # Mark the current node as visited and store in path 
        # Remove current vertex from path[] and mark it as unvisited 
        # current path[] 
        else: 
        if u ==d: 
        path.append(u) 
        path.pop() 
        visited[u]= False
        visited[u]= True
    def printAllPathsUtil(self, u, d, visited, path): 
   
   
    # Prints all paths from 's' to 'd' 
    def printAllPaths(self,s, d): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 
  
        # Create an array to store paths 
        path = [] 
  
        # Call the recursive helper function to print all paths 
        self.printAllPathsUtil(s, d,visited, path) 
   
   
   
# Create a graph given in the above diagram 
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 3) 
g.addEdge(2, 0) 
g.addEdge(2, 1) 
g.addEdge(1, 3) 
   
s = 2 ; d = 3
print ("Following are all different paths from %d to %d :" %(s, d)) 
g.printAllPaths(s, d) 