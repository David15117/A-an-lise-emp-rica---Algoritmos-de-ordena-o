import matplotlib.pyplot



# movimentações realizadas

valores = [499500,12497500,49995000,199990000,1249975000,4999950000]
tempo = [0.253322,7.138416,30.799624,106.739968,562.483109,2239.320178]
matplotlib.pyplot.title('Insertions Sort - Decrescente ')
matplotlib.pyplot.xlabel('Movimentações realizadas')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
