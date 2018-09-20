import time
from Agente import Agente

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
		hn = raw_input()	
		v = input("snmpVersion: ")
		ip = raw_input("IP: ")
		puerto = input("Puerto: ")
		comunidad = raw_input("Comunidad: ")
		indice = 0
		lista_agentes.append(Agente(indice, hn, v, ip, puerto, comunidad)) 	
		print(lista_agentes[0].getComunidad())		
		if numAgentes >= 1:
                	print(lista_agentes[1].getComunidad())
		numAgentes = numAgentes+1
		print("\n")
	
	elif opc == 2:
		print("Visualizar")

	elif opc == 3:
		print("Eliminar agente")

	elif opc == 4: 
		print("Estado de dispositivo")

	elif opc == 5: 
		print("Graficas")

	else: 
		print("Hasta luego! :'(")

