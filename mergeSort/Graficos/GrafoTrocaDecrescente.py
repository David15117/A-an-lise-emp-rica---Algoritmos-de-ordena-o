import matplotlib.pyplot



# movimentações realizadas

valores = [500,2500,5000,10000,25000,50000]
tempo = [0.140622,0.739027,1.374324,2.768601,7.595682,13.691379]
matplotlib.pyplot.title('Merge-Sort - Movimentações realizadas com vetor de valores inversamente ordenadas ')
matplotlib.pyplot.xlabel('Movimentações realizadas')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
