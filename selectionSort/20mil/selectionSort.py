import time
import matplotlib.pyplot
import psutil

#-------------------------------Aletatorio----------------------#
arq = open('20000Aleatorio.csv', 'r')
final = open('20000Aleatorio.txt', 'w')
linhas = arq.read()
linhas = linhas.split(';')

lista = []
for i in linhas:
    i = i.replace("\n", "")
    if(i != ''):
        lista.append(int(i))

tamanhoLista = len(lista)


def selectionSort(lista):
    tam = len(lista)-1
    qtdComparacoes = 0
    qtdTrocas = 0
    for i in range(0, tam):
        eleito = lista[i]
        menor = lista[i+1]
        pos = i+1
        for j in range(i+1, tam):
            if lista[j] < menor:
                menor = lista[j]
                pos = j
                qtdComparacoes += 1

        if menor < eleito:
            lista[i] = lista[pos]
            lista[pos] = eleito
            qtdComparacoes += 1
            qtdTrocas+=1
    usoCpu = psutil.cpu_percent()
    usoRam = psutil.virtual_memory()

    return usoCpu, usoRam, qtdComparacoes, qtdTrocas, lista
resultados=()
inicio = time.time()
resultados = selectionSort(lista)
fim = time.time()
tempExe = fim - inicio
print(len(lista))



final.write("\tSelection-sort\n"+"Quantidade de comparações: "+str(resultados[2])+"\nQuantidade de trocas: "+str(resultados[3])+"\nTempo de execução: "+str(tempExe)+"\nUso da CPU: "+str(resultados[0])+"\nUso de RAM: "+str(resultados[1])+"\nLista: "+str(resultados[4]))
final.close()

#-------------------------------Crescente----------------------#
arq = open('20000Crescente.csv', 'r')
final = open('20000Crescente.txt', 'w')
linhas = arq.read()
linhas = linhas.split(';')

lista = []
for i in linhas:
    i = i.replace("\n", "")
    if(i != ''):
        lista.append(int(i))

tamanhoLista = len(lista)


def selectionSort(lista):
    tam = len(lista)-1
    qtdComparacoes = 0
    qtdTrocas = 0
    for i in range(0, tam):
        eleito = lista[i]
        menor = lista[i+1]
        pos = i+1
        for j in range(i+1, tam):
            if lista[j] < menor:
                menor = lista[j]
                pos = j
                qtdComparacoes += 1

        if menor < eleito:
            lista[i] = lista[pos]
            lista[pos] = eleito
            qtdComparacoes += 1
            qtdTrocas+=1
    usoCpu = psutil.cpu_percent()
    usoRam = psutil.virtual_memory()

    return usoCpu, usoRam, qtdComparacoes, qtdTrocas, lista
resultados=()
inicio = time.time()
resultados = selectionSort(lista)
fim = time.time()
tempExe = fim - inicio
print(len(lista))



final.write("\tSelection-sort\n"+"Quantidade de comparações: "+str(resultados[2])+"\nQuantidade de trocas: "+str(resultados[3])+"\nTempo de execução: "+str(tempExe)+"\nUso da CPU: "+str(resultados[0])+"\nUso de RAM: "+str(resultados[1])+"\nLista: "+str(resultados[4]))
final.close()

#-------------------------------Decrescente----------------------#
arq = open('20000Decrescente.csv', 'r')
final = open('20000Decrescente.txt', 'w')
linhas = arq.read()
linhas = linhas.split(';')

lista = []
for i in linhas:
    i = i.replace("\n", "")
    if(i != ''):
        lista.append(int(i))

tamanhoLista = len(lista)


def selectionSort(lista):
    tam = len(lista)-1
    qtdComparacoes = 0
    qtdTrocas = 0
    for i in range(0, tam):
        eleito = lista[i]
        menor = lista[i+1]
        pos = i+1
        for j in range(i+1, tam):
            if lista[j] < menor:
                menor = lista[j]
                pos = j
                qtdComparacoes += 1

        if menor < eleito:
            lista[i] = lista[pos]
            lista[pos] = eleito
            qtdComparacoes += 1
            qtdTrocas+=1
    usoCpu = psutil.cpu_percent()
    usoRam = psutil.virtual_memory()

    return usoCpu, usoRam, qtdComparacoes, qtdTrocas, lista
resultados=()
inicio = time.time()
resultados = selectionSort(lista)
fim = time.time()
tempExe = fim - inicio
print(len(lista))



final.write("\tSelection-sort\n"+"Quantidade de comparações: "+str(resultados[2])+"\nQuantidade de trocas: "+str(resultados[3])+"\nTempo de execução: "+str(tempExe)+"\nUso da CPU: "+str(resultados[0])+"\nUso de RAM: "+str(resultados[1])+"\nLista: "+str(resultados[4]))
final.close()