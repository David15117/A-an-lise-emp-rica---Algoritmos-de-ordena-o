import matplotlib.pyplot



# movimentações realizadas

valores = [499500,12497500,49995000,199990000,1249975000,4999950000]
tempo = [0.418877,20.343790,42.749617,203.828046,1226.855309,4934.022500]
matplotlib.pyplot.title('Bubble Sort - Movimentações realizadas com vetor de valores inversamente ordenadas  ')
matplotlib.pyplot.xlabel('Movimentações realizadas')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
