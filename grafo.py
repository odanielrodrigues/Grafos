from random import randint
import math
class Grafo:

    #inicia o grafo com a matriz de peso das arestas com valores pre-definidos como -1
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
        self.matriz_pesos = [[math.inf] * self.vertices for _ in range(self.vertices)]
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
                self.matriz_pesos[u][v] = randint(pesomin,pesomax)

    def adiciona_aresta_teste(self, u,v, peso):

        #verifica se já existe essa ligação no grafo
        if v in self.grafo[u]:
            return
        #verifica se  u - v são diferentes
        else:
            if u != v:
                self.grafo[u].append(v)
                self.numero_arestas = self.numero_arestas + 1
                self.matriz_pesos[u][v] = peso

    #imprime a lista de ligaçoes e a matriz de pesos
    def mostra_lista_e_distancias(self):
        print("Lista de Vizinhanca")
        for i in range(self.vertices):
            print(f'{i} : -> ',  end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')
        #print("Matriz de Pesos")
        #for i in range(self.vertices):
        #    for j in range(self.vertices):
        #        print(self.matriz_pesos[i][j], end='  -  ')
        #    print('')

    def get_grafo(self):
        return self.grafo

def produzir_matriz_de_adjacencia(grafo):

    vertices = grafo.vertices
    matriz = [[int(0)] * vertices for _ in range(vertices)]

    for i in range(vertices):
        for j in range(int(grafo.grafo.__getitem__(i).__len__())):
            x = grafo.grafo[i][j]
            matriz[i][x] = 1

    return matriz

def mostrar_matriz_adjacencia(matriz):

    print("Matriz de Adjacencia")
    for i in range(len(matriz)):
         for j in range(len(matriz)):
            print(matriz[i][j], end='   ')
         print('')

def iniciar_grafo_aleatorio(numero_de_vertices, quantidade_de_aresta, pesomin, pesomax):

    grafo = Grafo(numero_de_vertices)
    while (grafo.numero_arestas < int(quantidade_de_aresta)):
        grafo.adiciona_aresta(randint(0,numero_de_vertices-1),randint(0,numero_de_vertices-1),pesomin,pesomax)

    else:
        print("Grafo gerado com sucesso!")
        print("Quantidade de Vertices: ", grafo.vertices)
        print("Quantidade de Arestas: ",grafo.numero_arestas)
    return grafo

def gerador_de_dist_pred(vertices):

    dist = []
    pred = []

    for _ in range(vertices):
        dist.append(math.inf)
        pred.append(None)

    return dist,pred
