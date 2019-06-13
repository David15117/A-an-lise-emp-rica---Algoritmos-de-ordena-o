import matplotlib.pyplot



#número de comparações vs tempo

valores = [500,2500,5000,10000,25000,50000]
tempo = [0.140622,0.739027,1.374324,2.768601,7.595682,13.691379]
matplotlib.pyplot.title('Merge-Sort - Número de comparação com vetor de valores inversamente ordenadas e ')
matplotlib.pyplot.xlabel('Número de comparações')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
