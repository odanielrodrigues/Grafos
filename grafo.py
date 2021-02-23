from random import randint
class Grafo:

    #inicia o grafo com a matriz de peso das arestas com valores pre-definidos como -1
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
        self.matriz_pesos = [[-1] * self.vertices for _ in range(self.vertices)]
        self.numero_arestas = 0

    def adiciona_aresta(self, u,v, pesomin,pesomax):

        #verifica se já existe essa ligação no grafo
        if v in self.grafo[u]:
            return
        #verifica se  u - v são diferentes
        else:
            if u != v:
                self.grafo[u].append(v)
                self.numero_arestas = self.numero_arestas + 1
                self.matriz_pesos[u][v]  = randint(pesomin,pesomax)

    #imprime a lista de ligaçoes e a matriz de pesos
    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i} : -> ',  end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.matriz_pesos[i][j], end='  -  ')
            print('')

    def get_grafo(self):
        return self.grafo

def matriz_adj(grafo):

    vertices = grafo.vertices
    matriz = [[int(0)] * vertices for _ in range(vertices)]

    for i in range(vertices):
        for j in range(int(grafo.grafo.__getitem__(i).__len__())):
            x = grafo.grafo[i][j]
            matriz[i][x] = 1

    for i in range(vertices):
      for j in range(vertices):
            print(matriz[i][j], end='             ')
      print('')

    return matriz

def adiciona_arestas_aleatorias(numero_de_vertices, quantidade_de_aresta, pesomin, pesomax):

    grafo = Grafo(numero_de_vertices)
    while (grafo.numero_arestas < int(quantidade_de_aresta)):
        grafo.adiciona_aresta(randint(0,numero_de_vertices-1),randint(0,numero_de_vertices-1),pesomin,pesomax)

    else:
        print("x")

    return grafo


G = adiciona_arestas_aleatorias(5,10,1,50)
G.mostra_lista()
matriz_adj(G)
print(G.numero_arestas)
#adiciona_arestas_aleatorias(grafo,10,1,50)
#G = adiciona_arestas_aleatorias(5,10,1,40)
