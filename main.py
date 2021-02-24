import dijkstra
from grafo import *

print("Vamos inicializar o grafo com os valores (Vertices, Arestas, PesoMin, PesoMax)")

print("Digite a quantidade de vertices:")
vertices = input()
print("Digite a quantidade de arestas:")
arestas = input()
print("Digite o peso minimo entre as arestas:")
pesoMin = input()
print("Digite o peso maximo entre as arestas:")
pesoMax = input()

#verifica se o peso minimo não é maior que o peso maximo
while pesoMin>pesoMax:
    print("O peso minimo não pode ser maior que o peso maximo, digite novamente")
    pesoMax = input()
    if pesoMax>pesoMin:
        break
else:
    #inicializa o grafo e a m1atriz de pesos com os paremetros passados pelo usuario e inicializa a matriz de adjacencias
    G = iniciar_grafo_aleatorio(int(vertices), int(arestas), int(pesoMin), int(pesoMax))
    MATRIZ_ADJ = produzir_matriz_de_adjacencia(G)
    #G.mostra_lista_e_distancias()
    #mostrar_matriz_adjacencia(MATRIZ_ADJ)
    dist, pred  = dijkstra.dijkstra_algoritmo(G.grafo,0,G.matriz_pesos)

    print("Arestas ->", G.numero_arestas)
    print("Vertices -> ", G.vertices)
    print(dist)
    print(pred)

