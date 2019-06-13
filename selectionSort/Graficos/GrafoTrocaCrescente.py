import matplotlib.pyplot



# movimentações realizadas

valores = [0,0,0,0,0,0]
tempo = [0.042882,1.461091,4.964721,19.078003,100.335626,400.812899]
matplotlib.pyplot.title('Selection-sort - Movimentações realizadas com vetor de valores já ordenados  ')
matplotlib.pyplot.xlabel('Movimentações realizadas')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
