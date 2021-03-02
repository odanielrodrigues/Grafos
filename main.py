import dijkstra
import bellmanford
import floydwarshall
import time
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

#MENU PRINCIPAL
while selecionar_tipo_de_grafo == None:
    selecionar_tipo_de_grafo = int(input("Modo: "))
    if selecionar_tipo_de_grafo > 2 or selecionar_tipo_de_grafo < 1:
        print("***Numero selecionado foi invalido, digite novamente***")
        selecionar_tipo_de_grafo = None
    else:
        #DEFINE SE O GRAFO VAI SER GERADO ALEATORIAMENTE E PEDE OS REQUISITOS PARA O USUARIO
        if selecionar_tipo_de_grafo == 1:
            print("---------------------VERTICES-------------------------------")
            vertices = int(input("Digite a quantidade de vertices para gerar um grafo aleatorio: "))
            if vertices == 0 or vertices <0:
                print("***O NUMERO DE VERTICE NÃO PODE SER NEGATIVO OU IGUAL A 0, REINICIE O PROGRAMA***")
                exit(1)

            verifica_possibilidade = int(vertices * (vertices - 1))
            print("Numero maximo possivel de arestas orientadas: ",verifica_possibilidade)
            if verifica_possibilidade == 0:
                print("***NÃO É POSSIVEL ADICIONAR NENHUMA ARESTA ORIENTADA, REINICIE O PROGRAMA***")
                exit(1)

            print("------------------------------------------------------------")
            print("----------------------ARESTAS-------------------------------")
            aresta = int(input("Digite a quantidade de arestas para gerar arestas aleatorias: "))

            if aresta == 0 or aresta <0:
                print("***UM GRAFO NÃO PODE POSSUIR UMA QUANTIDADE DE ARESTAS NEGATIVAS, E OS ALGORITMOS NÃO FUNCIONAM PARA UM GRAFO COM 0 ARESTAS, REINICIE O PROGRAMA***")
                exit(1)

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

        #CASO O GRAFO NÃO FOR ALEATORIO O USUARIO INSERE MANUALMENTE O TAMANHO E A QUANTIDADE DE ARESTAS DO GRAFO
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
    #APOS O GRAFO SER GERADO COM SUCESSO, PERGUNTA AO USUARIO SE QUER VER A LISTA DE ADJ E MATRIZ DE PESOS
    print("Deseja imprimir o grafo [Lista de Vizinhaça, Matriz de Peso]? ")
    verifica = int(input("1 - Sim, qualquer outro numero não imprimira o grafo: "))
    print("--------------------------------------------------------------")

    while verifica == int(1):
        G.mostra_lista_e_distancias()
        G.mostrar_matriz_de_pesos()
        verifica = None
    print("--------------------------------------------------------------")

    selecao = None

    #DISPONIBILIZA PRO USUARIO A SELEÇÃO DO ALGORITMO DESEJADO PARA REALIZAR OS TESTES
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

            #PAINEL DO ALGORITMO APOS SER SELECIONADO, PERGUNTA O USUARIO QUAL CAMINHO DEVE SER FEITO E VALIDA O CAMINHO RETORNANDO O RESULTADO CASO FOR POSIVEL
            if selecao == 1:

                print(">-----------------------------------------------Dijkstra------------------------------------------------------<")
                print("EI, VAMOS FAZER UM CAMINHO??")

                aux = True
                while aux == True:

                    origem = int(input("Digite a origem: "))
                    destino = int(input("Digite o destino: "))
                    if origem > G.grafo.__len__()-1 or origem < 0 or destino < 0 or destino > G.grafo.__len__()-1:
                        print("Destino ou caminho excede o tamanho permitido tente novamente")
                    else:
                        tempo = time.time()
                        dist, pred = dijkstra.dijkstra_algoritmo(G.grafo, origem, G.matriz_pesos)
                        tempo = time.time() - tempo
                        print("TEMPO GASTO DE EXECUÇÃO: ", tempo)
                        print("----------------------------------LISTA DE DIST/PRED---------------------------------------------------")
                        print(dist)
                        print(pred)
                        print("-------------------------------------------------------------------------------------------------------")
                        aux = False

                print(">--------------------------------------------------------------------------------------------------------------<")
                print("LISTA DE CAMINHO RECUPERADO")
                print(recuperar_caminho_lista(origem, destino, pred))
                print("PESO: ", dist[destino])
                print(">--------------------------------------------------------------------------------------------------------------<")

                quero_testar_novamente = int(input("DESEJA TESTAR O MESMO GRAFO EM ALGUM OUTRO ALGORITMO? 1 - Sim, qualquer outro numero não:  "))
                if quero_testar_novamente == 1:
                    selecao = None

                print(">--------------------------------------------------------------------------------------------------------------<")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("\n\n\n")

            elif selecao == 2:
                print(">----------------------------------------------Bellman-Ford-----------------------------------------------------<")
                print("EI, VAMOS FAZER UM CAMINHO??")

                aux = True
                while aux == True:

                    origem = int(input("Digite a origem: "))
                    destino = int(input("Digite o destino: "))
                    if origem > G.grafo.__len__() - 1 or origem < 0 or destino < 0 or destino > G.grafo.__len__() - 1:
                        print("Destino ou caminho excede o tamanho permitido tente novamente")
                    else:
                        tempo = time.time()
                        dist, pred = bellmanford.bellman_ford_algoritmo(G.grafo, origem, G.lista_aresta_pesos)
                        tempo = time.time() - tempo
                        print("----------------------------------LISTA DE DIST/PRED---------------------------------------------------")
                        print(dist)
                        print(pred)
                        print("-------------------------------------------------------------------------------------------------------")
                        print("TEMPO GASTO DE EXECUÇÃO: ", tempo)
                        aux = False

                print(">--------------------------------------------------------------------------------------------------------------<")
                print("LISTA DE CAMINHO RECUPERADO")
                print(recuperar_caminho_lista(origem, destino, pred))
                print("PESO: ", dist[destino])
                print(">--------------------------------------------------------------------------------------------------------------<")

                quero_testar_novamente = int(input("DESEJA TESTAR O MESMO GRAFO EM ALGUM OUTRO ALGORITMO? 1 - Sim, qualquer outro numero não:  "))
                if quero_testar_novamente == 1:
                    selecao = None

                print(">--------------------------------------------------------------------------------------------------------------<")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("\n\n\n")

            else:
                print(">-----------------------------------------------Floyd-Warshall-------------------------------------------------<")
                print("EI, VAMOS FAZER UM CAMINHO??")

                aux = True
                while aux == True:

                    origem = int(input("Digite a origem: "))
                    destino = int(input("Digite o destino: "))
                    if origem > G.grafo.__len__() - 1 or origem < 0 or destino < 0 or destino > G.grafo.__len__() - 1:
                        print("Destino ou caminho excede o tamanho permitido tente novamente")
                    else:

                        tempo = time.time()
                        dist, pred = floydwarshall.floydwarshall_algoritmo(G.matriz_pesos)
                        tempo = time.time() - tempo
                        print("---------------------------------------------------------------------------------------------------------------")
                        mostrar_matriz_pred_dist_floyd(dist,pred)
                        print(">--------------------------------------------------------------------------------------------------------------<")
                        print("TEMPO GASTO DE EXECUÇÃO: ", tempo)
                        aux = False

                print(">--------------------------------------------------------------------------------------------------------------<")
                print("LISTA DE CAMINHO RECUPERADO")
                print(recuperar_caminho_matriz(origem, destino, pred))
                print("PESO: ", dist[origem][destino])

                quero_testar_novamente = int(input("DESEJA TESTAR O MESMO GRAFO EM ALGUM OUTRO ALGORITMO? 1 - Sim, qualquer outro numero não:  "))
                if quero_testar_novamente == 1:
                    selecao = None

                print(">--------------------------------------------------------------------------------------------------------------<")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("\n\n\n")

    #APOS O PROGRAMA SER FINALIZADO OU ECONTRAR UM EXIT(1)
    else:
        print("--------------------------------------------FIM DO PROGRAMA-----------------------------------------------------")