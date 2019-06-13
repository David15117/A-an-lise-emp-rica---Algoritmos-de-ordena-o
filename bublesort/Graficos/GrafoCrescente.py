import matplotlib.pyplot

#n=x
#t=y

valores = [1000,5000,10000,20000,50000,100000]
tempo = [0.222403,6.618840,28.743983,129.208867,660.944389,2311.806743]
matplotlib.pyplot.title('Bubble Sort - Vetor de valores já ordenados  ')
matplotlib.pyplot.xlabel('Número de elementos')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
