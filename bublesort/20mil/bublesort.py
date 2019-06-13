import time #biblioteca time do python
import psutil  #biblioteca responsavel por pegar informçãoes da CPU,memorria, disco, network, sensors)
arq = open('20000Decrescente.csv', 'r') # csv
final = open('20000Decrescente.txt', 'w')#alterar aqui para gerar os resultados para os diferentes algoritmos


linhas = arq.read() #ler linhas
linhas = linhas.split(';') # Separando os dados de linhas com split

lista = []
for i in linhas:
    i = i.replace("\n", "")
    if(i != ''):
        lista.append(int(i))

tamanhoLista = len(lista) #tamanho da lista

#____________ Algoritmo Bubble Short__________
def bubbleSort(lista):
    qtdComparacoes = 0  #Variavel para identificar quantidade de comrações
    qtdTrocas = 0 #Variavel para identificar quantidade de variações
    for j in range(len(lista)):
        for i in range(len(lista)-1):
            qtdComparacoes += 1 # Acrscenta valores a variavel
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                qtdTrocas+=1
    usoCpu = psutil.cpu_percent()
    usoRam = psutil.virtual_memory()
    return usoCpu, usoRam, qtdComparacoes, qtdTrocas,  lista


def bubbleSortMelhoria1(lista):
    qtdComparacoes = 0
    qtdTrocas = 0
    for j in range(len(lista)):
        for i in range(len(lista)-1, j, -1):
            qtdComparacoes += 1
            if lista[i] < lista[i-1]:
                aux = lista[i]
                lista[i] = lista[i-1]
                lista[i-1] = aux
                
                qtdTrocas+=1
    usoCpu = psutil.cpu_percent()
    usoRam = psutil.virtual_memory()
    return usoCpu, usoRam, qtdComparacoes, qtdTrocas,  lista

#dimenuindo a complexibilidade  pois deixei de utilizar 1 for  para usar while
def bubbleSortMelhoria2(lista):
    j=1
    troca=True
    tam = len(lista)-1
    qtdComparacoes = 0
    qtdTrocas = 0
    while (j<=tam) and troca:
        tempoinicio = time.time()
        troca = False
        for i in range(tam, j-1, -1):
            qtdComparacoes += 1
            if lista[i]<lista[i-1]:
                troca=True
                aux = lista[i]
                lista[i] = lista[i-1]
                lista[i-1] = aux
               
                qtdTrocas+=1
        j+=1
    usoCpu = psutil.cpu_percent()
    usoRam = psutil.virtual_memory()
    return usoCpu, usoRam, qtdComparacoes, qtdTrocas, lista

resultados=()
inicio = time.time()
resultados = bubbleSort(lista)#depois de gerado o txt com as informações do primeiro algoritmo, altere aqui para gerar as informações sobre os outros algoritmos. Na linha 6 mude o arquivo resultante
fim = time.time()
tempExe = fim - inicio
print(len(lista))
#plt.plot(VTempo)
#plt.title("Tempo gasto por operação")
#plt.show()
final.write("\tBubble Sort\n\nQuantidade de comparações: "+str(resultados[2])+"\nQuantidade de trocas: "+str(resultados[3])+"\nTempo de execução: "+str(tempExe)+"\nUso da CPU: "+str(resultados[0])+"\nUso de RAM: "+str(resultados[1])+"\nLista: "+str(resultados[4]))
final.close()
