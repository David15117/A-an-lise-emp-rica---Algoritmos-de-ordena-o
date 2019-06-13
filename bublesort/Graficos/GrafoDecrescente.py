import matplotlib.pyplot
#n=x
#t=y

valores = [999000,24995000,99990000,399980000,2499950000,9999900000]
tempo = [0.418877,20.343790,42.749617,203.828046,1226.855309,4934.022500]
matplotlib.pyplot.title('Bubble Sort - Vetor de valores inversamente ordenadas ')
matplotlib.pyplot.xlabel('Número de elementos')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()


