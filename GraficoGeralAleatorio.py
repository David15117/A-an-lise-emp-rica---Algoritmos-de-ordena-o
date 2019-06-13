import matplotlib.pyplot as plt

x = [1000,5000,10000,20000,50000,100000]
bublesort = [0.423864,16.319370,34.171872,133.337103,997.711105,3433.514416]
insertion = [0.133,3.898,15.302,55.438,295.854,1363.87]
merge = [0.162564,0.690153,1.393272,2.805495,6.829732,13.691379]
selection = [0.041917,1.933661,5.393574,18.694997,120.043913,462.315930]
quick   = [0.011961, 0.044878, 0.096742, 0.180518, 0.604384, 1.123994]
yBar = [1000,5000,10000,20000,50000,100000]
z = [i * 1.5 for i in yBar]
xBar = range(len(yBar))

plt.xlabel('Relação número de elementos ')
plt.ylabel('Tempo gasto na ordenação em segundos ')
plt.title('COMPARAÇÃO ENTRE OS ALGORITMOS DE ORDENAÇÃO')
plt.plot(x, bublesort , color='#0000CD', label ='BubleSort')
plt.plot(x, insertion , color='#00FFFF',label ='InsertonSort')
plt.plot(x, merge, color='#00FF00',label ='MergeSort')
plt.plot(x, selection , color='#D2691E',label ='SelectionSort')
plt.plot(x, quick , color='#FF00FF',label ='QuickSort')
plt.legend()
plt.show()