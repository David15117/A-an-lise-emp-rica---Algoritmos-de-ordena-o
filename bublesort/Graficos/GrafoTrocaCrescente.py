import matplotlib.pyplot



# movimentações realizadas

valores = [0,0,0,0,0,0]
tempo = [0.222403,6.618840,28.743983,129.208867,660.944389,2311.806743]
matplotlib.pyplot.title('Bubble Sort - Movimentações realizadas com vetor de valores já ordenados ')
matplotlib.pyplot.xlabel('Movimentações realizadas')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
