from random import randint, shuffle, choice
import random
#-------------- Aleatorio-----------------#
tamanho = 1000000 #<========= digite o valor tamanho da lista
#-------------- Descrecente-----------------#
arq = open(str(tamanho)+'Decrescente'+'.csv', 'w')

result = list(range(tamanho))
print(result)

for i in result[::-1]:
    arq.write((str(result[i]))+';\n')

arq.close()
#-------------- Crescente-----------------#
arq = open(str(tamanho)+'Crescente'+'.csv', 'w')

result = list(range(tamanho))
print(result)

for i in result:
    arq.write((str(result[i]))+';\n')

arq.close()

#-------------- Aletario-----------------#
arq = open(str(tamanho)+'Aleatorio'+'.csv', 'w')

result = list(range(tamanho))
shuffle(result)

print(result)

for i in result:
    arq.write((str(result[i]))+';\n')

arq.close()