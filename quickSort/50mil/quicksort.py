import time
import matplotlib.pyplot
import psutil
#----------------------------Aleatorio-----------------------#
arq = open('50000Aleatorio.csv', 'r')
final = open('50000Aleatorio.txt', 'w')

linhas = arq.read()
linhas = linhas.split(';')

lista = []
for i in linhas:
    i = i.replace("\n", "")
    if(i != ''):
        lista.append(int(i))

tamanhoLista = len(lista)
usoCpu = psutil.cpu_percent()
usoRam = psutil.virtual_memory()
qtdComparacoes = 0
qtdTrocas  = 0

def quicksort(x):
    tempoinicio = time.time()
    global qtdComparacoes
    global  qtdTrocas
    if len(x) == 1 or len(x) == 0:
        return x

    else:
        pivo = x[0]
        i = 0
        for j in range(len(x)-1):

            if x[j+1] < pivo:
                qtdComparacoes += 1
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        qtdTrocas += 1
        primeira_parte = quicksort(x[:i])
        segunda_parte = quicksort(x[i+1:])
        primeira_parte.append(x[i])
        lista = primeira_parte + segunda_parte
        return lista



resultados=()
inicio = time.time()
resultados = quicksort(lista)
fim = time.time()
tempExe = fim - inicio
print(qtdTrocas)
print(qtdComparacoes)
print(len(lista))

final.write("Quick Sort\n"+"Quantidade de comparações: "+str(qtdComparacoes)+"\nQuantidade de trocas: "+str(qtdTrocas)+"\nTempo de execução: "+str(tempExe)+"\nUso da CPU: "+str(usoCpu)+"\nUso de RAM: "+str(usoRam)+"\nLista: "+str(resultados))
final.close()
