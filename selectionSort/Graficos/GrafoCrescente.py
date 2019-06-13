import matplotlib.pyplot

#n=x
#t=y

valores = [1000,5000,10000,20000,50000,100000]
tempo = [0.042882,1.461091,4.964721,19.078003,100.335626,400.812899]
matplotlib.pyplot.title('Selection-sort - Vetor de valores já ordenados  ')
matplotlib.pyplot.xlabel('Número de elementos')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
