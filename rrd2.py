import time
import rrdtool
from getSNMP import consultaSNMP


total_input_traffic = 0
total_output_traffic = 0


def validarEstadoAgente(comunidad,ip):
	estado=int(consultaSNMP(comunidad, ip, '1.3.6.1.2.1.2.2.1.7.2'))
	return estado
	
def status(comunidad, ip):
	indice = int(consultaSNMP(comunidad,ip,'1.3.6.1.2.1.2.2.1.8.2'))
	return indice

def getIndiceInterfaz(comunidad, ip):
	indice = consultaSNMP(comunidad, ip, '1.3.6.1.2.1.4.20.1.2' +ip)
	return indice
total_input_traffic = int(
        consultaSNMP('SNMPcomunidad','localhost',
                     '1.3.6.1.2.1.2.2.1.10.3'))
    total_output_traffic = int(
        consultaSNMP('SNMPcomunidad','localhost',
                     '1.3.6.1.2.1.2.2.1.16.3'))
    total_input_Ipv4 = int(
        consultaSNMP('SNMPcomunidad','localhost',
                     '1.3.6.1.2.1.2.2.1.16.3'))

    total_output_Ipv4 = int(
        consultaSNMP('SNMPcomunidad','localhost',
                     '1.3.6.1.2.1.2.2.1.16.3'))

    total_input_Icmp = int(
        consultaSNMP('SNMPcomunidad','localhost',
                     '1.3.6.1.2.1.2.2.1.16.3'))

    total_output_Icmp = int(
        consultaSNMP('SNMPcomunidad','localhost',
                     '1.3.6.1.2.1.2.2.1.16.3'))

    total_input_IP = int(
        consultaSNMP('SNMPcomunidad','localhost',
                     '1.3.6.1.2.1.2.2.1.16.3'))

    total_output_IP = int(
        consultaSNMP('SNMPcomunidad','localhost',
                     '1.3.6.1.2.1.2.2.1.16.3'))

    total_input_Snmp = int(
        consultaSNMP('SNMPcomunidad','localhost',
                     '1.3.6.1.2.1.2.2.1.16.3'))
    total_output_Snmp = int(
        consultaSNMP('SNMPcomunidad','localhost',
                     '1.3.6.1.2.1.2.2.1.16.3'))
valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
valor1 = "N:"+ str(total_input_Ipv4)':'+ str(total_output_Ipv4)
valor2 = "N" + str(total_input_Icmp)':' + str(total_output_Icmp)
valor3 = "N" + str(total_input_IP)':' + str(total_output_IP)'
Valor4 ="N" +  str(total_input_Snmp)':'  + str(total_output_Snmp)
    print valor
    rrdtool.update('net3.rrd', valor)
    rrdtool.update('net4.rrd', valor1)
    rrdtool.update('net5.rrd', valor2)
    rrdtool.update('net6.rrd', valor3)
    rrdtool.update('net7.rrd', valor4)
    rrdtool.dump('net3.rrd','net3.xml')
    rrdtool.dump('net4.rrd','net4.xml')
    rrdtool.dump('net5.rrd','net5.xml')
    rrdtool.dump('net6.rrd','net6.xml')
    rrdtool.dump('net7.rrd','net7.xml')
    time.sleep(1)

if ret:
    print rrdtool.error()
    time.sleep(300)


"""
status1_connect = 0;
status_connect2 = 0;

num_interfaces_red = 0;
num_interfaces_red2 = 0;

status_interfaces = 0;
status_interfaces = 0;
"""
"""
num_dispo2_monotorizados = int(consultaSNMP('Fer','localhost','1.3.6.1.2.1.2.2.1.16.3'))
valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
print valor
"""
"""
total_input_traffic = int(consultaSNMP('Fer','localhost','1.3.6.1.2.1.2.2.1.10.3'))
total_output_traffic = int(consultaSNMP('Fer','localhost','1.3.6.1.2.1.2.2.1.16.3'))
valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
print valor

total_input_traffic = int(consultaSNMP('Fer','localhost','1.3.6.1.2.1.2.2.1.10.3'))
total_output_traffic = int(consultaSNMP('Fer','localhost','1.3.6.1.2.1.2.2.1.16.3'))
valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
print valor

total_input_traffic = int(consultaSNMP('Fer','localhost','1.3.6.1.2.1.2.2.1.10.3'))
total_output_traffic = int(consultaSNMP('Fer','localhost','1.3.6.1.2.1.2.2.1.16.3'))
valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
print valor
"""
"""while 1:
    total_input_traffic = int(
        consultaSNMP('Fer','localhost',
                     '1.3.6.1.2.1.2.2.1.10.3'))
    total_output_traffic = int(
        consultaSNMP('Fer','localhost',
                     '1.3.6.1.2.1.2.2.1.16.3'))

    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    print valor
    rrdtool.update('net3.rrd', valor)
    rrdtool.dump('net3.rrd','net3.xml')
    time.sleep(1)
"""
"""
if ret:
    print rrdtool.error()
    time.sleep(300)
"""
