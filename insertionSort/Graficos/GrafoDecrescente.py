import matplotlib.pyplot
#n=x
#t=y

valores = [1000,5000,10000,20000,50000,100000]
tempo = [0.253322,7.138416,30.799624,106.739968,562.483109,2239.320178]
matplotlib.pyplot.title('Insertions Sort - inversamente ordenadas ')
matplotlib.pyplot.xlabel('Número de elementos')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()


