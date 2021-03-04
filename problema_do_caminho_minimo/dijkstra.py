from grafo import *
import math

def dijkstra_algoritmo(grafo, origem, matriz_de_pesos):

    dist, pred = gerador_de_dist_pred(grafo.__len__()) #funçao que instancia a lista de dist (infinita) e pred (vazios)
    dist[origem] = 0
    Q = [i for i in range(grafo.__len__())]

    while Q:

        menor = math.inf
        u = -1
        for v in Q:                     # Extrai a menor distancia presente
            if dist[v] < menor:         # na lista Q
                menor = dist[v]
                u = v
        if u == -1:
            break
        Q.remove(u)

        for v in grafo[u]:              #laço principal
            if dist[v] > dist[u] + matriz_de_pesos[u][v]:
                dist[v] = dist[u] + matriz_de_pesos[u][v]
                pred[v] = u

    return dist,pred









