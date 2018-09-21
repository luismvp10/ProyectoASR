# -*- coding: utf-8 -*-
import time
from Agente import Agente
from estadoAgente import *
from rrd2 import *
import os
import time

numAgentes = 0
lista_agentes = []
print("\n")
print("Bienvenido a observium_patito")

while True:
    print("\nDispositivos monitoreados: "+ str(numAgentes)+"\n")
    print("Estas son las operaciones que puedes realizar")
    print("1.-Agregar agente")
    print("2.-Visualizar agentes")
    print("3.-Eliminar Agente")
    print("4.-Estado de dispositivo")
    print("5.-Graficas")
    print("\n")
    opc = input("Opcion:")


    if opc == 1:

        os.system('clear')
        print("Agregar Agente\n")
        id1 = numAgentes
        hn = raw_input("Hostname: ")
        v = input("snmpVersion: ")
        ip = raw_input("IP: ")
        puerto = input("Puerto: ")
        comunidad = raw_input("Comunidad: ")
        indice = getIndexInterface(comunidad,ip)
        print(indice)
        lista_agentes.append(Agente(id1, indice, hn, v, ip, puerto, comunidad))
        print(lista_agentes[0].getComunidad())
        if numAgentes >= 1:
                    print(lista_agentes[1].getComunidad())
        numAgentes = numAgentes+1
        print("\n")

    elif opc == 2:
        os.system('clear')
        print("Visualizar Agentes\n")
        print("ID  -- Hostname  -- IP")

        cont = 0
        if len(lista_agentes) == 0:
            print("Nada que visualizar")
        else:
            while cont < len(lista_agentes):
                print( str(lista_agentes[cont].getId()) + "      "+ str(lista_agentes[cont].getHostName())+ "      " +str(lista_agentes[cont].getIp()))

                print("\n")

                if status(lista_agentes[cont].getComunidad(),lista_agentes[cont].getIp()) == 1:
                    print("Status connection: up")
                else:
                    print("Status connection: down")
                    status =int(statusInterfaces(lista_agentes[cont].getComunidad(),lista_agentes[cont].getIp()))
                if status == 1:
                    print("Status interface: up")
                    num = int(getNumInterfacesRed(lista_agentes[cont].getComunidad(), lista_agentes[cont].getIp()))
                    print("Interfaces red disponibles: " + str(num))
                else:
                    print("Status interface: down")

                #print(str(status(lista_agentes[cont].getComunidad(),lista_agentes[cont].getIp())))
                cont = cont + 1

    elif opc == 3:
        os.system('clear')
        print("Eliminar agente")
        id1 = input("Ingresa id del agente a eliminar")
        lista_agentes.pop(id1)
    elif opc == 4:
            os.system('clear')
            print("Estado de dispositivos")
            print("\n")
            #print("ID  -- Hostname  -- IP")

            i = 0
            if len(lista_agentes) == 0:
                print("Nada que visualizar")
            else:
                while i< len(lista_agentes):
                    print("Agent ID: "+str(lista_agentes[i].getId()))
                    print("Hostname: "+str(lista_agentes[i].getHostName()) )
                    ip = lista_agentes[i].getIp()
                    comunidad = lista_agentes[i].getComunidad()
                    print("IP: "+str(lista_agentes[i].getIp()))
                    print("namePC: " +str(getAgentName(comunidad,ip)))
                    print("S.O: "+str(getOperativeSystem(comunidad, ip)))
                    print("Network Interfaces: "+str(getInterfacesNet(comunidad, ip)))
                    print("Activity time: "+getCompleteTime(str(getTimeActivity(comunidad, ip))))
                    print("Location: "+str(getAgentLocation(comunidad, ip)))
                    print("Contact: "+str(getContact(comunidad,ip)))




                    print("\n\n")
                    i = i + 1





    elif opc == 5:
            os.system('clear')
            print("Graficas")
            print("1.-Tráfico de Interfaz (I/O)")
            print("2.-Estádisticas de paquetes ipv4 (I/O)")
            print("3.-Estádisticas ICMP (I/O)")
            print("4.-Estádisticas IP (I/O)")
            print("5.-Estádisticas  de paquetes SNMP (I/O)")
            opcGraph =int(raw_input("Cuál desea visualizar? :"))
            id = input("ID del agente: ")
            if opcGraph == 1:
                print("Gráfica 1")
            elif opcGraph == 2:
                print("Gráfica 2")
            elif opcGraph == 3:
                print("Gráfica 3")
            elif opcGraph == 4:
                print("Gráfica 4")
            elif opcGraph == 5:
                print("Gráfica 5")
            else:
                print("Opción inválida")







    else:
        print("Hasta luego! :'(")

