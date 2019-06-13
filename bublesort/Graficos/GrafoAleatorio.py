import matplotlib.pyplot
#https://www.convertworld.com/pt/tempo/minutos.html converte resultado para minutos
#n=x
#t=y

valores = [1000,5000,10000,20000,50000,100000]
tempo = [0.423864,16.319370,34.171872,133.337103,997.711105,3433.514416]
matplotlib.pyplot.title('Bubble Sort - Vetor de valores aleatórios  ')
matplotlib.pyplot.xlabel('Número de elementos')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
