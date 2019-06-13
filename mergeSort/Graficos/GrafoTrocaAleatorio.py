import matplotlib.pyplot

# movimentações realizadas

valores = [500,2498,4997,10000,25000,49999]
tempo = [0.162564,0.690153,1.393272,2.805495,6.829732,13.691379]
matplotlib.pyplot.title('Merge-Sort - movimentos realizados com vetor de valores aleatórios')
matplotlib.pyplot.xlabel('Movimentações realizadas')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
