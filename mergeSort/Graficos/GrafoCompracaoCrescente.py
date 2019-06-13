import matplotlib.pyplot



#número de comparações vs tempo

valores = [500,2500,5000,10000,25000,50000]
tempo = [0.187498,0.822797,1.364352,2.655896,8.162168,13.841976]
matplotlib.pyplot.title('Merge-Sort - Número de comparação com vetor de valores já ordenados ')
matplotlib.pyplot.xlabel('Número de comparações')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
