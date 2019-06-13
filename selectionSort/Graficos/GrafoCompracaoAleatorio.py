import matplotlib.pyplot
import matplotlib.pyplot as plt
#número de comparações vs tempo

valores = [6115,40670,86664,188646,516232,1106124]
tempo = [0.041917,1.933661,5.393574,18.694997,120.043913,462.315930]
matplotlib.pyplot.title('Selection sort - vetor com valores aleatorio ')
matplotlib.pyplot.xlabel('Número de comparações')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
