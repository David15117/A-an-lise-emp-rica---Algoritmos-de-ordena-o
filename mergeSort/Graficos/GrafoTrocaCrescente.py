import matplotlib.pyplot



# movimentações realizadas

valores = [0,0,0,0,0,0]
tempo = [0.187498,0.822797,1.364352,2.655896,8.162168,13.841976]
matplotlib.pyplot.title('Merge-Sort - Movimentações realizadas com vetor de valores já ordenados ')
matplotlib.pyplot.xlabel('Movimentações realizadas')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
