# -*-coding:utf8 -*-
from random import * 
""" 
Générateur de niveau pour PyZen :

"""
# STATISTIQUES 

nb0=0
nbM=0

niveau=['0','m']
generation=[]
for i in range(1,223):
	generation.append(choice(niveau))
	if generation[-1] == '0':
		nb0+=1
	else:
		nbM+=1
	i+=1
print("le nombre de 0 est de :", nb0," et le nombre de M est de :",nbM)

generation[0]='d'
generation.append('a')
print(generation)
f=open('n1','w')

# Enregistrement de l'intégralité de la liste au sein d'un fichier externe
for element in generation:
	f.write(element)
f.close()
f=open('n1','rw')
for line in f:
	t=f.read(15)
	t.append('\n')
print(t)
f.close()
