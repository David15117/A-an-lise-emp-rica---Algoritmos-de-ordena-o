import matplotlib.pyplot
#https://www.convertworld.com/pt/tempo/minutos.html converte resultado para minutos
#n=x
#t=y

valores = [1000,5000,10000,20000,50000,100000]
tempo = [0.041917,1.933661,5.393574,18.694997,120.043913,462.315930]
matplotlib.pyplot.title('Selection-sort - Vetor de valores aleatórios ')
matplotlib.pyplot.xlabel('Número de elementos')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
