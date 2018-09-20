import time
from Agente import Agente
from rrd2 import *

numAgentes = 0
lista_agentes = []	
	 
print("Bienvenido a la calculadora")

while True:
	print("Dispositivos monitoreados: "+ str(numAgentes)+"\n")
	print("Estas son las operaciones que puedes realizar")
	print("1.-Agregsar agente")
	print("2.-Visualizar agentes")
	print("3.-Eliminar Agente")
	print("4.-Estado de dispositivo")
	print("5.-Graficas")
	opc = input("Opcion:")

	if opc == 1:
		print("Agregar Agente\n")
		id1 = numAgentes
		hn = raw_input()	
		v = input("snmpVersion: ")
		ip = raw_input("IP: ")
		puerto = input("Puerto: ")
		comunidad = raw_input("Comunidad: ")
		indice = 0
		print(indice)
		lista_agentes.append(Agente(id1, indice, hn, v, ip, puerto, comunidad)) 	
		print(lista_agentes[0].getComunidad())		
		if numAgentes >= 1:
                	print(lista_agentes[1].getComunidad())
		numAgentes = numAgentes+1
		print("\n")
	
	elif opc == 2:
		print("Visualizar")
		cont = 0
		while cont < len(lista_agentes):			
			print(str(lista_agentes[cont].getId()) + " " + str(lista_agentes[cont].getIp()))
			if status(lista_agentes[cont].getComunidad()) == 1:
				print("Status: up")
			else: 
				print("Status: down")
			#print(str(status(lista_agentes[cont].getComunidad(),lista_agentes[cont].getIp())))
			cont = cont + 1

	elif opc == 3:
		print("Eliminar agente")

	elif opc == 4: 
		print("Estado de dispositivo")

	elif opc == 5: 
		print("Graficas")

	else: 
		print("Hasta luego! :'(")

