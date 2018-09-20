import time
from Agente import Agente
		 
print("Bienvenido a la calculadora")

#while True:
print("Estas son las operaciones que puedes realizar")
print("1.-Agregsar agente")
print("2.-Visualizar agentes")
print("3.-Eliminar Agente")
print("4.-Estado de dispositivo")
print("5.-Graficas")
opc = input("OPcion:")
agente1 = Agente(0, "", 2,4,6,7)
if opc == 1:
	print("Agregar Agente")
	print(agente1.getIndex())
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

