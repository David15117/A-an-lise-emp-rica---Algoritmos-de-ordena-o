import matplotlib.pyplot

# movimentações realizadas

valores = [990,4990,9982,188646,49990,99985]
tempo = [0.041917,1.933661,5.393574,18.694997,120.043913,462.315930]
matplotlib.pyplot.title('Selection-sort - Movimentações realizadas com vetor de valores aleatórios  ')
matplotlib.pyplot.xlabel('Movimentações realizadas')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
