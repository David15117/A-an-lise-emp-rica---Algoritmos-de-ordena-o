import matplotlib.pyplot
import matplotlib.pyplot as plt
#número de comparações vs tempo

valores = [999000,24995000,99990000,399980000,2499950000,9999900000]
tempo = [0.423864,16.319370,34.171872,133.337103,997.711105,3433.514416]
matplotlib.pyplot.title('Bubble Sort - Comparação com vetor de valores aleatórios  ')
matplotlib.pyplot.xlabel('Número de comparações')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
