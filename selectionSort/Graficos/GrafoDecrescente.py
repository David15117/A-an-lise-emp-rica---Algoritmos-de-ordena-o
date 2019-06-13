import matplotlib.pyplot
#n=x
#t=y

valores = [1000,5000,10000,20000,50000,100000]
tempo = [0.071808,2.367633,10.259568,45.771573,179.229638,743.264613]
matplotlib.pyplot.title('Selection-sort - Vetor de valores inversamente ordenada ')
matplotlib.pyplot.xlabel('Número de elementos')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()


