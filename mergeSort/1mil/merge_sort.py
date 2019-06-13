import time
import psutil
#--------------------------------------Aleatorio------------------------
arq = open('1000Aleatorio.csv', 'r')
final = open('1000Aleatorio.txt', 'w')

linhas = arq.read()
linhas = linhas.split(';')

lista = []
for i in linhas:
    i = i.replace("\n", "")
    if(i != ''):
        lista.append(int(i))

tamanhoLista = len(lista)

def merge_sort(lista):
    qtdComparacoes = 0
    qtdTrocas = 0

    if len(lista) > 1:
        mid = len(lista) // 2
        left_half = lista[:mid]
        right_half =lista[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            tempoinicio = time.time()
            qtdComparacoes += 1
            if left_half[i] < right_half[j]:
                lista[k] = left_half[i]
                i += 1
            else:
                lista[k] = right_half[j]
                qtdTrocas += 1
                j += 1
            k += 1

        while i < len(left_half):
            lista[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lista[k] = right_half[j]
            j += 1
            k += 1

    ##print(lista) Vericando se a lista esta correta
    usoCpu = psutil.cpu_percent()
    usoRam = psutil.virtual_memory()

    return usoCpu, usoRam, qtdComparacoes, qtdTrocas , lista


resultados=()
inicio = time.time()
resultados = merge_sort(lista)
fim = time.time()
tempExe = fim - inicio

print(len(lista))


final.write("\tMerge-Sort\n"+"Quantidade de comparações: "+str(resultados[2])+"\nQuantidade de trocas: "+str(resultados[3])+"\nTempo de execução: "+str(tempExe)+"\nUso da CPU: "+str(resultados[0])+"\nUso de RAM: "+str(resultados[1])+"\nLista: "+str(resultados[4]))
final.close()
#--------------------------------------Descrescente------------------------
arq = open('1000Decrescente.csv', 'r')
final = open('1000Decrescente.txt', 'w')

linhas = arq.read()
linhas = linhas.split(';')

lista = []
for i in linhas:
    i = i.replace("\n", "")
    if(i != ''):
        lista.append(int(i))

tamanhoLista = len(lista)

def merge_sort(lista):
    qtdComparacoes = 0
    qtdTrocas = 0

    if len(lista) > 1:
        mid = len(lista) // 2
        left_half = lista[:mid]
        right_half =lista[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            tempoinicio = time.time()
            qtdComparacoes += 1
            if left_half[i] < right_half[j]:
                lista[k] = left_half[i]
                i += 1
            else:
                lista[k] = right_half[j]
                qtdTrocas += 1
                j += 1
            k += 1

        while i < len(left_half):
            lista[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lista[k] = right_half[j]
            j += 1
            k += 1

    ##print(lista) Vericando se a lista esta correta
    usoCpu = psutil.cpu_percent()
    usoRam = psutil.virtual_memory()

    return usoCpu, usoRam, qtdComparacoes, qtdTrocas , lista


resultados=()
inicio = time.time()
resultados = merge_sort(lista)
fim = time.time()
tempExe = fim - inicio

print(len(lista))


final.write("\tMerge-Sort\n"+"Quantidade de comparações: "+str(resultados[2])+"\nQuantidade de trocas: "+str(resultados[3])+"\nTempo de execução: "+str(tempExe)+"\nUso da CPU: "+str(resultados[0])+"\nUso de RAM: "+str(resultados[1])+"\nLista: "+str(resultados[4]))
final.close()

#--------------------------------------Crescente------------------------
arq = open('1000Crescente.csv', 'r')
final = open('1000Crescente.txt', 'w')

linhas = arq.read()
linhas = linhas.split(';')

lista = []
for i in linhas:
    i = i.replace("\n", "")
    if(i != ''):
        lista.append(int(i))

tamanhoLista = len(lista)

def merge_sort(lista):
    qtdComparacoes = 0
    qtdTrocas = 0

    if len(lista) > 1:
        mid = len(lista) // 2
        left_half = lista[:mid]
        right_half =lista[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            tempoinicio = time.time()
            qtdComparacoes += 1
            if left_half[i] < right_half[j]:
                lista[k] = left_half[i]
                i += 1
            else:
                lista[k] = right_half[j]
                qtdTrocas += 1
                j += 1
            k += 1

        while i < len(left_half):
            lista[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lista[k] = right_half[j]
            j += 1
            k += 1

    ##print(lista) Vericando se a lista esta correta
    usoCpu = psutil.cpu_percent()
    usoRam = psutil.virtual_memory()

    return usoCpu, usoRam, qtdComparacoes, qtdTrocas , lista


resultados=()
inicio = time.time()
resultados = merge_sort(lista)
fim = time.time()
tempExe = fim - inicio

print(len(lista))


final.write("\tMerge-Sort\n"+"Quantidade de comparações: "+str(resultados[2])+"\nQuantidade de trocas: "+str(resultados[3])+"\nTempo de execução: "+str(tempExe)+"\nUso da CPU: "+str(resultados[0])+"\nUso de RAM: "+str(resultados[1])+"\nLista: "+str(resultados[4]))
final.close()

