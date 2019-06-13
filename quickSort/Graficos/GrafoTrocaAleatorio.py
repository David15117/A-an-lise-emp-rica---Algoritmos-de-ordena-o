import matplotlib.pyplot

# movimentações realizadas

valores = [668,3346,6688,13327,33379,66755,200234,399911,600457]
tempo = [0.011961, 0.044878, 0.096742, 0.180518, 0.604384, 1.123994,5.383602,10.559755,16.626530]
matplotlib.pyplot.title('Quick Sort - movimentações realizadas com vetor de valores aleatórios  ')
matplotlib.pyplot.xlabel('Movimentações realizadas')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
