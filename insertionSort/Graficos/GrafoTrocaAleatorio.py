import matplotlib.pyplot

# movimentações realizadas

valores = [247706,6302074,25039054,100781006,624375510,2506406276]
tempo = [0.133,3.898,15.302,55.438,295.854,1363.87]
matplotlib.pyplot.title('Insertions Sort - Movimentações realizadas com valores Aleatorio ')
matplotlib.pyplot.xlabel('Movimentações realizadas')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
