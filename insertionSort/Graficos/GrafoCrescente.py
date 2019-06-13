import matplotlib.pyplot

#n=x
#t=y

valores = [1000,5000,10000,20000,50000,100000]
tempo = [0.000996,0.000997,0.00498,0.00897,0.01495,0.03291]
matplotlib.pyplot.title('Insertions Sort - Estruturas já ordenadas ')
matplotlib.pyplot.xlabel('Número de elementos')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
