import time
import rrdtool
from getSNMP import consultaSNMP


total_input_traffic = 0
total_output_traffic = 0


def validarEstadoAgente(comunidad,ip):
	estado=int(consultaSNMP(comunidad, ip, '1.3.6.1.2.1.2.2.1.7.2'))
	return estado
	
def num_dispo():
	num_dispo1_monotorizados = 0
	num_dispo2_monotorizados = 0
	num_dispo_monotorizados = int(consultaSNMP('Fer','localhost','1.3.6.1.2.1.2.2.1.10.3'))
	return num_dispo_monotorizados

def getIndiceInterfaz(comunidad, ip):
	indice = consultaSNMP(comunidad, ip, '1.3.6.1.2.1.4.20.1.2' +ip)
	return indice 
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
