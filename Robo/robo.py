class Graph: 
    def __init__(self, coord, coord2, dist): 
        self.graph = {}
        self.r1 = coord   # coordenadas do robo 1
        self.r2 = coord2  # coordenadas do robo 2
        self.dist = dist  # distancia minima entre os robos 

    def findPaths(self, r, d):
        path = [] # array p guardar caminhos
        visited = {}
        robotTurn = 0
        for no in self.graph:
            visited[no] = False
        self.findPathsAux(r, d, visited, path, robotTurn)
        
    def findPathsAux(self, r, d, visited, path, robotTurn):
        print("VEZ: ", robotTurn)
        aux = robotTurn
        if robotTurn == 0:
            robotTurn += 1
        elif robotTurn == 1:
            robotTurn -= 1
        visited[r[aux]] = True
        path.append(r[aux])
        # se ja chegou no destino printa
        if r[aux] == d[aux]:# and self.isSecureDistance(r):
            print("Caminho encontrado: ", path, "\n")
        else:
            for i in self.graph[r[aux]]:
                if visited[i] == False:
                    newR = (i, r[1])
                    if aux == 1:
                        newR = (r[0], i)
                    print(newR)
                    self.findPathsAux(newR, d, visited, path, robotTurn)
        # Deleta nodo atual de path e marca como nodo visitado
        path.pop() 
        visited[r[aux]] = False

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
                #if (i, j) == self.r1 or (i, j) == self.r2:
                 #   print("Robot", self.graph[(i, j)])
                #else:
                 #   print((i, j), self.graph[(i, j)])
            

# Testes
g = Graph((0, 0), (2, 2), 1) # origens
g.initGrid(3)
print("ROBO 1")
g.findPaths((g.r1, g.r2), ((0, 2), (2, 1))) # possibilidades