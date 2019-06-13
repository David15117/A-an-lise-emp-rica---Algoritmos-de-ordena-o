import matplotlib.pyplot



#número de comparações vs tempo

valores = [999000,24995000,99990000,399980000,2499950000,9999900000]
tempo = [0.222403,6.618840,28.743983,129.208867,660.944389,2311.806743]
matplotlib.pyplot.title('Bubble Sort - Número de comparação com vetor de valores já ordenados')
matplotlib.pyplot.xlabel('Número de comparações')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
