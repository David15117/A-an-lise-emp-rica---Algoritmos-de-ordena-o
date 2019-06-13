import matplotlib.pyplot



# movimentações realizadas

valores = [500,2500,5000,10000,25000,50000]
tempo = [0.071808,2.367633,10.259568,45.771573,179.229638,743.264613]
matplotlib.pyplot.title('Selection-sort - Movimentações realizadas com vetor de valores inversamente ordenadas  ')
matplotlib.pyplot.xlabel('Movimentações realizadas')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
