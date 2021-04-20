import algoritmos_e_funçoes
import sys
import time


print("---------------------------------TP02 -TEORIA DOS GRAFOS -----------------------------")

# VARIAVEIS PARA VALORES PADROES
vertices = int(input("Número de vértices: "))
pesoMin = int(input("Peso mínimo das arestas: "))
pesoMax = int(input("Peso máxima das arestas: "))
grafo = None

if vertices <= 0 or pesoMin <= 0 or pesoMax <= 0:
    sys.exit("Os valores não podem ser igual a 0, porfavor reinicie o programa!")
if pesoMin <= pesoMax:
    grafo = algoritmos_e_funçoes.criarGrafoMatriz(vertices, pesoMin, pesoMax)
else:
    sys.exit("Peso Maximo não pode ser maior que o peso minimo, porfavor reinicie o programa!")

imprimir = int(input("Deseja imprimir o grafo? 1 - Sim // Qualquer numero para - Não: "))

if imprimir == 1:
    algoritmos_e_funçoes.mostrar_matriz_adjacencia(grafo)

#VARIAVEL PARA AUXILIO NA SELECAO DO ALGORITMO DESEJADO
selecao = None

#DISPONIBILIZA PARA O USUARIO A SELEÇÃO DO ALGORITMO PARA REALIZAR OS TESTES
while selecao == None:

    print("SELECIONE O ALGORITMO QUE DESEJA APLICA O GRAFO")
    print("1 - Algoritmo Heuristico - Vizinho Mais Próximo (GULOSO)")
    print("2 - Algoritmo Força-Bruta")
    selecao = int(input("Algoritmo: "))

    if selecao > 2 or selecao <1:
        print("***NUMERO SELECIONADO FOI INVALIDO, DIGITE NOVAMENTE***")
        selecao = None
    else:

        if selecao == 1:

            print("---------------Algoritmo Guloso do Vizinho Mais Próximo---------------")
            tempo = time.time()
            ciclo = algoritmos_e_funçoes.vizinhoMaisProximo(grafo)
            tempo = time.time() - tempo
            custo = algoritmos_e_funçoes.recuperaCusto(ciclo,grafo)
            print("Rota: ", ciclo, "\nCusto: ", custo, "\nTempo: ", tempo)

            quero_testar_novamente = int(input("DESEJA TESTAR O MESMO GRAFO EM ALGUM OUTRO ALGORITMO? 1 - Sim, qualquer outro numero NÃO:  "))
            if quero_testar_novamente == 1:
                selecao = None
        else:

            print("---------------Algoritmo de Força-Bruta---------------")
            tempo = time.time()
            ciclo = algoritmos_e_funçoes.forcaBruta(grafo)
            tempo = time.time() - tempo
            custo = algoritmos_e_funçoes.recuperaCusto(ciclo,grafo)
            print("Rota: ", ciclo, "\nCusto: ", custo, "\nTempo: ", tempo)

            quero_testar_novamente = int(
                input("DESEJA TESTAR O MESMO GRAFO EM ALGUM OUTRO ALGORITMO? 1 - Sim, qualquer outro numero NÃO:  "))
            if quero_testar_novamente == 1:
                selecao = None

print("----------------------------FIM DO PROGRAMA!!----------------------------")
