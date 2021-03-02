from grafo import *
import math
def floydwarshall_algoritmo(matriz_de_pesos):

    dist, pred = cria_matriz_dist_pred(matriz_de_pesos.__len__())

    for i in range(matriz_de_pesos.__len__()):
        for j in range(matriz_de_pesos.__len__()):
            if i == j:
                dist[i][j] = 0
            elif matriz_de_pesos[i][j] != math.inf:
                dist[i][j] = matriz_de_pesos[i][j]
                pred[i][j] = i
            else:
                dist[i][j] = math.inf
                pred[i][j] = None


    for k in range(matriz_de_pesos.__len__()):
        for i in range(matriz_de_pesos.__len__()):
            for j in range(matriz_de_pesos.__len__()):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred