from random import randint
import math
class Grafo:

    #inicia o grafo com a matriz de peso das arestas com valores pre-definidos para facilitar a execução dos algoritmos
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
        self.matriz_pesos = [[math.inf] * self.vertices for _ in range(self.vertices)]
        self.lista_aresta_pesos =[]
        self.numero_arestas = 0

    #adiciona uma aresta aleatoria (u,v) com peso aleatorio
    def adiciona_aresta(self, u,v, pesomin,pesomax):

        if v in self.grafo[u]:
            return

        else:
            if u != v:
                peso = randint(pesomin,pesomax)
                self.grafo[u].append(v)
                self.numero_arestas = self.numero_arestas + 1
                self.matriz_pesos[u][v] = float(peso)
                self.lista_aresta_pesos.append([int(u),int(v),float(peso)])

    #utilizado apra adicionar arestas manualmente no grafo (teste de verificação)
    def adiciona_aresta_teste(self, u, v, peso):

        if u > (self.matriz_pesos.__len__()-1) or u < 0 or v > (self.matriz_pesos.__len__()-1) or v < 0:
            print("Não pode ser adicionado, regra de tamanho")
            return False
        else:

            if v in self.grafo[u]:
                print("Não pode ser adicionado - Já existente")
                return False

            else:
                if u != v:
                    self.grafo[u].append(v)
                    self.numero_arestas = self.numero_arestas + 1
                    self.matriz_pesos[u][v] = float(peso)
                    self.lista_aresta_pesos.append([int(u),int(v),float(peso)])

                    print("Adicionado com sucesso!")
                    return True
                else:
                    print("Não pode ser adicionado - São iguais")

    #imprime a lista de ligaçoes e a matriz de pesos
    def mostra_lista_e_distancias(self):
        print("Lista de Vizinhanca - Grafo")
        for i in range(self.vertices):
            print(f'{i} : -> ',  end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

    #Imprime matriz de pesos
    def mostrar_matriz_de_pesos(self):

        print("Matriz de Pesos - Grafo")
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.matriz_pesos[i][j], end='  -  ')
            print('')

    def get_grafo(self):
        return self.grafo

#Gera uma matriz de adjacencia baseada em um Grafo G
def produzir_matriz_de_adjacencia(grafo):

    vertices = grafo.vertices
    matriz = [[0] * vertices for _ in range(vertices)]

    for i in range(vertices):
        for j in range(int(grafo.grafo.__getitem__(i).__len__())):
            x = grafo.grafo[i][j]
            matriz[i][x] = 1

    return matriz

#Cria matriz de Dist Pred com INF e NONE para auxiliar nos algoritmos
def cria_matriz_dist_pred(tamanho):

    dist = [[math.inf for i in range(int(tamanho))] for j in range(int(tamanho))]
    pred = [[None for i in range(int(tamanho))] for j in range(int(tamanho))]


    return  dist,pred

#Imprime Matriz de Adjacencia
def mostrar_matriz_adjacencia(matriz):

    print("Matriz de Adjacencia")
    for i in range(len(matriz)):
         for j in range(len(matriz)):
            print(matriz[i][j], end='   ')
         print('')

#Imprime matriz de Pred Dist no algorimo floyd
def mostrar_matriz_pred_dist_floyd(dist,pred):

    print(">>>>>Matriz de Distancia<<<<<")
    for i in range(dist.__len__()):
        for j in range(dist.__len__()):
            print(dist[i][j], end='    ')
        print('')

    print("\n\n\n")

    print(">>>>>Matriz de Pred<<<<<")
    for i in range(pred.__len__()):
        for j in range(pred.__len__()):
            print(pred[i][j], end='    ')
        print('')

#Gera um grafo aleatorio para auxiliar nos algoritmos
def iniciar_grafo_aleatorio(numero_de_vertices, quantidade_de_aresta, pesomin, pesomax):

    grafo = Grafo(numero_de_vertices)
    while (grafo.numero_arestas < int(quantidade_de_aresta)):
        grafo.adiciona_aresta(randint(0,numero_de_vertices-1),randint(0,numero_de_vertices-1),pesomin,pesomax)

    else:
        print("GRAFO GERADO COM SUCESSO!!")

    return grafo

#Gera 2 listas dist e pred com valores INF e NONE para auxiliar os algoritmos
def gerador_de_dist_pred(vertices):

    dist = []
    pred = []

    for _ in range(vertices):
        dist.append(math.inf)
        pred.append(None)


    return dist,pred

#Recuperar caminhos minimos Matriz e Lista, valida a possibilidade do caminho
def recuperar_caminho_matriz(origem,destino,matriz_pred):

    if matriz_pred[origem][destino] == None:
        print("***ESSE CAMINHO NÃO É POSSIVEL***")
    else:
        caminho = []
        aux = destino

        while aux != origem:

            caminho.append(matriz_pred[origem][aux])
            aux = matriz_pred[origem][aux]

        caminho.reverse()
        return caminho

def recuperar_caminho_lista(origem,destino,lista_pred):

    if lista_pred[destino] == None:
        print("***ESSE CAMINHO NÃO É POSSIVEL***")
    else:

        caminho = []
        aux = destino

        while aux != origem:
            aux = lista_pred[aux]
            caminho.append(aux)

        caminho.reverse()

        return caminho

