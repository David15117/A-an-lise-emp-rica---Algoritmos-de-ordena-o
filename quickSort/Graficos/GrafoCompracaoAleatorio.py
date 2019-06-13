import matplotlib.pyplot
import matplotlib.pyplot as plt
#número de comparações vs tempo

valores = [5092,38812,85943,158896,505425,989909,3489514,7285345,10875958]
tempo = [0.011961, 0.044878, 0.096742, 0.180518, 0.604384, 1.123994,5.383602,10.559755,16.626530]
matplotlib.pyplot.title('Quick Sort - Comparação com vetor de valores aleatórios ')
matplotlib.pyplot.xlabel('Número de comparações')
matplotlib.pyplot.ylabel('Tempo gasto na ordenação  em Segundos')
matplotlib.pyplot.plot(valores,tempo)
matplotlib.pyplot.show()
