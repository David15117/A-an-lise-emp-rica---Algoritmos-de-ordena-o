import matplotlib.pyplot



#número de comparações vs tempo

valores = [249501,6247501,24995001,99990001,624975001,2499950001]
tempo = [0.071808,2.367633,10.259568,45.771573,179.229638,743.264613]
matplotlib.pyplot.title('Selection-sort - Comparação com vetor de valores inversamente ordenadas ')
matplotlib.pyplot.xlabel('Número de comparações')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
