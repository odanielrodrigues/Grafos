import dijkstra
import bellmanford
import floydwarshall
import math
from grafo import *
print("Vamos começar..")
print("Deseja criar um grafo e introduzir os valores, ou gerar tudo aleatoriamente? ")
print("1 - Criar aleatorio")
print("2 - Introduzir manualmente")

selecionar_tipo_de_grafo = None
vertices = None
aresta = None
pesomin = None
pesomax = None
G = None
pred = math.inf
dist = math.inf
verifica_possibilidade = 0


while selecionar_tipo_de_grafo == None:
    selecionar_tipo_de_grafo = int(input("Modo: "))
    if selecionar_tipo_de_grafo > 2 or selecionar_tipo_de_grafo < 1:
        print("***Numero selecionado foi invalido, digite novamente***")
        selecionar_tipo_de_grafo = None
    else:

        if selecionar_tipo_de_grafo == 1:
            print("---------------------VERTICES-------------------------------")
            vertices = int(input("Digite a quantidade de vertices para gerar um grafo aleatorio: "))

            verifica_possibilidade = int(vertices * (vertices - 1))
            print("Numero maximo possivel de arestas orientadas: ",verifica_possibilidade)
            print("------------------------------------------------------------")

            print("----------------------ARESTAS-------------------------------")
            aresta = int(input("Digite a quantidade de arestas para gerar arestas aleatorias: "))

            while aresta > verifica_possibilidade:
                if aresta > verifica_possibilidade:
                    print("***Não é possivel gerar um grafo com essa quantiadde de aresta, tente novamente!***")
                    aresta = int(input("Digite a quantidade de arestas para gerar arestas aleatorias: "))

            else:
                print("------------------------------------------------------------")
                print("------------------------PESOS-------------------------------")
                pesomin = float(input("Digite o peso minimo para as arestas geradas aleatoriamente: "))
                pesomax = float(input("Digite o peso maxímo para as arestas geradas aleatoriamente: "))

                while pesomin > pesomax:
                    if pesomin > pesomax:
                        print("***Não é possivel gerar peso minimo maior que peso maximo, tente novamente!***")
                        pesomax = int(input("Digite o peso maximo novamente: "))
                else:
                    print("--------------------------------------------------------------")
                    print("O GRAFO ALEATORIO ESTA SENDO GERADO COM OS SEGUINTES ATRIBUTOS")
                    print("Vertices: ", vertices)
                    print("Arestas: ", aresta)
                    print("Peso Minimo: ", pesomin)
                    print("Peso Maximo: ",pesomax)
                    G = iniciar_grafo_aleatorio(vertices, aresta, pesomin, pesomax)

                    print("--------------------------------------------------------------")

        else:
            print("---------------------VERTICES-------------------------------")
            vertices = int(input("Digite a quantidade de vertices para gerar um grafo: "))
            verifica_possibilidade = int(vertices * (vertices - 1))
            print("Numero maximo possivel de arestas orientadas: ", verifica_possibilidade)
            G = Grafo(vertices)
            print("Grafo Criado com Sucesso")
            print("------------------------------------------------------------")

            digitando_arestas = int(1)

            while digitando_arestas == int(1):
                print("Digite os valores da aresta orientada:")
                G.adiciona_aresta_teste(int(input("u -> ")),int(input("v -> ")), float(input("Peso - > ")))
                if G.numero_arestas == verifica_possibilidade:
                    print("Numero Maximo de arestas adicionadas")
                    print("------------------------------------------------------------")
                    break
                else:
                    digitando_arestas = int(input("Deseja adicionar uma aresta?  1 - Sim , Qualquer outro valor - Não -->  "))
            else:
                print("...")
else:

    print("Deseja imprimir o grafo [Lista de Vizinhaça, Matriz de Peso]? ")
    verifica = int(input("1 - Sim, qualquer outro numero não imprimira o grafo: "))
    print("--------------------------------------------------------------")

    while verifica == int(1):
        G.mostra_lista_e_distancias()
        G.mostrar_matriz_de_pesos()
        verifica = None
    print("--------------------------------------------------------------")


    selecao = None

    while selecao == None:
        quero_testar_novamente = 0
        print("SELECIONE O ALGORITMO QUE DESEJA APLICAR NO GRAFO")
        print("1 - Dijkstra")
        print("2 - Bellman-ford")
        print("3 - Floyd-Warshall")
        selecao = int(input("Algoritmo: "))

        if selecao > 3 or selecao < 1:
            print("***Numero selecionado foi invalido, digite novamente***")
            selecao = None
        else:

            if selecao == 1:
                print(">-----------------------------------------------Dijkstra------------------------------------------------------<")
                dist, pred = dijkstra.dijkstra_algoritmo(G.grafo, 0, G.matriz_pesos)
                print(dist)
                print(pred)
                print(">--------------------------------------------------------------------------------------------------------------<")
                quero_testar_novamente = int(input("DESEJA TESTAR O MESMO GRAFO EM ALGUM OUTRO ALGORITMO? 1 - Sim, qualquer outro numero não:  "))
                if quero_testar_novamente == 1:
                    selecao = None

                print(">--------------------------------------------------------------------------------------------------------------<")
            elif selecao == 2:
                print(">----------------------------------------------Bellman-Ford-----------------------------------------------------<")
                dist, pred = bellmanford.bellman_ford_algoritmo(G.grafo, 0, G.lista_aresta_pesos)
                print(dist)
                print(pred)
                print(">--------------------------------------------------------------------------------------------------------------<")

                quero_testar_novamente = int(input("DESEJA TESTAR O MESMO GRAFO EM ALGUM OUTRO ALGORITMO? 1 - Sim, qualquer outro numero não:  "))
                if quero_testar_novamente == 1:
                    selecao = None

                print(">--------------------------------------------------------------------------------------------------------------<")

            else:
                print(">-----------------------------------------------Floyd-Warshall-------------------------------------------------<")
                dist, pred = floydwarshall.floydwarshall_algoritmo(G.matriz_pesos)
                print(dist)
                print(pred)
                print(">--------------------------------------------------------------------------------------------------------------<")

                quero_testar_novamente = int(input("DESEJA TESTAR O MESMO GRAFO EM ALGUM OUTRO ALGORITMO? 1 - Sim, qualquer outro numero não:  "))
                if quero_testar_novamente == 1:
                    selecao = None


    else:
        print("--------------------------------------------FIM DO PROGRAMA-----------------------------------------------------")