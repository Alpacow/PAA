from collections import defaultdict 


class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) # grafo = dicionário com listas de vertices

    def DFS(self, v): 
        explored = [False] * (len(self.graph)) # seta todos os vertices como não visitados
        # chama recursivamente a funçao auxiliar
        # que marca os nodos visitados
        self.Explored(v, explored) 
  
    def Explored(self, v, explored): 
        explored[v] = True # seta o nodo atual como Visitado
        print(v, self.graph[v]) 
        # Realiza a recursão para percorrer os vertices adjacentes
        for i in self.graph[v]: 
            if explored[i] == False: # se não foi explorado chama recursão
                self.Explored(i, explored)

    def AddEdge(self, u, v): 
        self.graph[u].append(v) 
  

# Testes
g = Graph() 
g.AddEdge(0, 1) 
g.AddEdge(0, 2)
g.AddEdge(0, 3)
g.AddEdge(1, 2) 
g.AddEdge(2, 0)
g.AddEdge(3, 3)
g.AddEdge(2, 4)
g.AddEdge(4, 4)
  
print("DFS - Início: 0") 
g.DFS(0) 
