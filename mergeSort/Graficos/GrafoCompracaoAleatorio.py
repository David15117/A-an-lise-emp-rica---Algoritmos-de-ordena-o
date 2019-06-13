import matplotlib.pyplot

#número de comparações vs tempo

valores = [998,4998,9997,19999,49998,99999]
tempo = [0.162564,0.690153,1.393272,2.805495,6.829732,13.691379]
matplotlib.pyplot.title('Merge-Sort - Comparação com vetor de valores aleatórios  ')
matplotlib.pyplot.xlabel('Número de comparações')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
