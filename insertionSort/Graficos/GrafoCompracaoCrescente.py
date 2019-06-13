import matplotlib.pyplot



#número de comparações vs tempo

valores = [0,0,0,0,0,0]
tempo = [0.000996,0.000997,0.00498,0.00897,0.01495,0.03291]
matplotlib.pyplot.title('Insertions Sort - Comparação valores já ordenadas ')
matplotlib.pyplot.xlabel('Número de comparações')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
