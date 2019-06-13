import matplotlib.pyplot
#https://www.convertworld.com/pt/tempo/minutos.html converte resultado para minutos
#n=x
#t=y

valores = [1000,5000,10000,20000,50000,100000]
tempo = [0.162564,0.690153,1.393272,2.805495,6.829732,13.691379]
matplotlib.pyplot.title('Merge-Sort - Vetor de valores aleatórios ')
matplotlib.pyplot.xlabel('Número de elementos')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
