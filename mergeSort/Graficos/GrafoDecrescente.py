import matplotlib.pyplot
#n=x
#t=y

valores = [1000,5000,10000,20000,50000,100000]
tempo = [0.140622,0.739027,1.374324,2.768601,7.595682,13.691379]
matplotlib.pyplot.title('Merge-Sort - Vetor de valores inversamente ordenadas  ')
matplotlib.pyplot.xlabel('Número de elementos')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()


