import matplotlib.pyplot

#n=x
#t=y

valores = [1000,5000,10000,20000,50000,100000]
tempo = [0.187498,0.822797,1.364352,2.655896,8.162168,13.841976]
matplotlib.pyplot.title('Merge-Sort - Vetor de valores já ordenados  ')
matplotlib.pyplot.xlabel('Número de elementos')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
