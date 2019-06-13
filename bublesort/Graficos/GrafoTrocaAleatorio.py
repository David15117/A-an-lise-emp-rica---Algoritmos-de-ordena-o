import matplotlib.pyplot

# movimentações realizadas

valores = [247706,6302074,25039054,100781006,624375510,2506406276]
tempo = [0.423864,16.319370,34.171872,133.337103,997.711105,3433.514416]
matplotlib.pyplot.title('Bubble Sort - movimentações realizadas com vetor de valores aleatórios  ')
matplotlib.pyplot.xlabel('Movimentações realizadas')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
