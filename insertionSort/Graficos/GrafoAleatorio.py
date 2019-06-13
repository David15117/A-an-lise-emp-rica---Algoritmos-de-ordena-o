import matplotlib.pyplot
#https://www.convertworld.com/pt/tempo/minutos.html converte resultado para minutos
#n=x
#t=y

valores = [1000,5000,10000,20000,50000,100000]
tempo = [0.133,3.898,15.302,55.438,295.854,1363.87]
matplotlib.pyplot.title('Insertions Sort - movimentações realizadas com valores Aleatorio ')
matplotlib.pyplot.xlabel('Número de elementos')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
