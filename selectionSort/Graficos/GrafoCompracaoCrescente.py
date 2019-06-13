import matplotlib.pyplot



#número de comparações vs tempo

valores = [0,0,0,0,0,0]
tempo = [0.042882,1.461091,4.964721,19.078003,100.335626,400.812899]
matplotlib.pyplot.title('Selection-sort - Comparação com vetor de valores já ordenados  ')
matplotlib.pyplot.xlabel('Número de comparações')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
