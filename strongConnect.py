from collections import defaultdict 


class Graph: 
    def __init__(self, nrV): 
        self.graph = defaultdict(list) # grafo = dicionário com listas de vertices
        self.V = nrV

    def DFS(self, v, graph): 
        explored = [False] * (self.V) # seta todos os vertices como não visitados
        # chama recursivamente a funçao auxiliar
        # que marca os nodos visitados
        self.Explored(v, explored, graph)
        return False if False in explored else True
  
    def Explored(self, v, explored, graph): 
        explored[v] = True # seta o nodo atual como Visitado
        print(v, graph[v])
        print(explored)
        # Realiza a recursão para percorrer os vertices adjacentes
        for i in graph[v]: 
            if explored[i] == False: # se não foi explorado chama recursão
                self.Explored(i, explored, graph)

    def ReverseGraph(self):
        newG = Graph(self.V)
        for i in self.graph: 
            for j in self.graph[i]: 
                newG.AddEdge(j,i)
        return newG

    def AddEdge(self, u, v): 
        self.graph[u].append(v)

    def isStrongConnect(self, init):
        if self.DFS(init, self.graph):
            newG = self.ReverseGraph()
            return self.DFS(init, newG.graph)
        return False


# Testes
g = Graph(5) 
g.AddEdge(0, 1); 
g.AddEdge(1, 2); 
g.AddEdge(2, 3); 
g.AddEdge(3, 0); 
g.AddEdge(2, 4); 
g.AddEdge(4, 2);
print("Fortemente conectado\n" if g.isStrongConnect(0) else "Não fortemente conectado\n")
  
g2 = Graph(4) 
g2.AddEdge(0, 1) 
g2.AddEdge(1, 2) 
g2.AddEdge(2, 3)
print ("Fortemente conectado\n" if g2.isStrongConnect(0) else "Não fortemente conectado\n")
