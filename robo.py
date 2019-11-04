class Graph: 
    def __init__(self, coord, coord2, dist): 
        self.graph = {}
        self.r1 = coord   # coordenadas do robo 1
        self.r2 = coord2  # coordenadas do robo 2
        self.dist = dist  # distancia minima entre os robos 

    def findPaths(self, r, r2, d):
        path = [] # array p guardar caminhos
        visited = {}
        for no in self.graph:
            visited[no] = False
        self.findPathsAux(r, r2, d, visited, path) 
        
    def findPathsAux(self, r, r2, d, visited, path):
        visited[r] = True
        path.append(r)
  
        # se ja chegou no destino printa
        if r == d and self.isSecureDistance(r, r2):
            print(path, "\n")
        else:
            for i in self.graph[r]:
                if visited[i] == False:
                    self.findPathsAux(i, r2, d, visited, path)             
        # Deleta nodo atual de path e marca como nodo visitado
        path.pop() 
        visited[r] = False

    def pointDistance(self, r1, r2):
        return r2 - r1 if r2 > r1 else r1 - r2

    def isSecureDistance(self, r1, r2):
        dx = self.pointDistance(r1[0], r2[0])
        dy = self.pointDistance(r1[1], r2[1])
        return (dx + dy) > self.dist

    def initGrid(self, x):
        for i in range(0, x):
            for j in range(0, x):
                self.graph[(i, j)] = []
                if i > 0 and i <= x - 1:
                    self.graph[(i, j)].append((i - 1, j))
                if j > 0 and j <= x - 1:
                    self.graph[(i, j)].append((i, j - 1))
                if i < x - 1 and i >= 0:
                    self.graph[(i, j)].append((i + 1, j))
                if j < x - 1 and j >= 0:
                    self.graph[(i, j)].append((i, j + 1))
                # Print Grid
                if (i, j) == self.r1 or (i, j) == self.r2:
                    print("Robot", self.graph[(i, j)])
                else:
                    print((i, j), self.graph[(i, j)])
            

# Testes
g = Graph((0, 0), (2, 2), 1) # origens
g.initGrid(3)
print("ROBO 1")
g.findPaths(g.r1, g.r2, (0, 1)) # possibilidades robo 1
#print("ROBO 2")
#g.findPaths(g.r2, (2, 0)) # possibilidades robo 2
#g.findPaths(g.r1, (0, 1), g.r2,  (2, 0)) # possibilidades robo 2