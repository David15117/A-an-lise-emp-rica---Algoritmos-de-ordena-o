import matplotlib.pyplot
#https://www.convertworld.com/pt/tempo/minutos.html converte resultado para minutos
#n=x
#t=y

valores = [1000,5000,10000,20000,50000,100000,300000,600000,900000]
tempo = [0.011961, 0.044878, 0.096742, 0.180518, 0.604384, 1.123994,5.383602,10.559755,16.626530]

matplotlib.pyplot.title('Quick Sort - Vetor de valores aleatórios ')
matplotlib.pyplot.xlabel('Número de elementos')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
