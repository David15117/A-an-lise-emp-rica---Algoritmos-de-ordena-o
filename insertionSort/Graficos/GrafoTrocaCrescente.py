import matplotlib.pyplot



# movimentações realizadas

valores = [0,0,0,0,0,0]
tempo = [0.000996,0.000997,0.00498,0.00897,0.01495,0.03291]
matplotlib.pyplot.title('Insertions Sort - movimentações realizadas em estrutura já ordenadas ')
matplotlib.pyplot.xlabel('Movimentações realizadas')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
