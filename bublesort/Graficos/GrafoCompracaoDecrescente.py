import matplotlib.pyplot



#número de comparações vs tempo

valores = [249501,6247501,24995001,99990001,624975001,2499950001]
tempo = [0.418877,20.343790,42.749617,203.828046,1226.855309,4934.022500]
matplotlib.pyplot.title('Bubble Sort - Número de comparação com vetor de valores inversamente ordenadas  ')
matplotlib.pyplot.xlabel('Número de comparações')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
