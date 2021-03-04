from grafo import *

def bellman_ford_algoritmo(grafo,origem,lista_aresta_peso):

    dist, pred = gerador_de_dist_pred(grafo.__len__())
    dist[origem] = 0

    for i in range(grafo.__len__()-1):
        trocou = False

        for e in lista_aresta_peso:
            if dist[e[1]] > dist[e[0]] + e[2]:
                dist[e[1]] = dist[e[0]] + e[2]
                pred[e[1]] = e[0]
                trocou = True

        if not trocou:
            break;

    return dist,pred
