import time
import rrdtool
from getSNMP import consultaSNMP

def getAgentName(comunidad,ip):
	name = consultaSNMP(comunidad, ip, '1.3.6.1.2.1.1.5.0')
	return name

def getOperativeSystem(comunidad,ip):
    so = consultaSNMP(comunidad, ip, '1.3.6.1.2.1.1.1.0')
    return so

def getInterfacesNet(comunidad,ip):
    noInterface = int(consultaSNMP(comunidad, ip, '1.3.6.1.2.1.2.1.0'))
    return  noInterface

def getTimeActivity(comunidad, ip):
    time = consultaSNMP(comunidad, ip, '1.3.6.1.2.1.1.3.0')
    return time

def getAgentLocation(comunidad,ip):
    location = consultaSNMP(comunidad, ip, '1.3.6.1.2.1.1.6.0')
    return location

def getContact(comunidad,ip):
    contact = consultaSNMP(comunidad, ip, '1.3.6.1.2.1.1.4.0')
    return contact


def getCompleteTime(nums):
    num = int(nums)/100
    hor = (int(num / 3600))
    minu = int((num - (hor * 3600)) / 60)
    seg = num - ((hor * 3600) + (minu * 60))
    res= str(hor) + "h " + str(minu) + "m " + str(seg) + "s"
    return res


def getIndexInterface(comunidad,ip):
    oid= '1.3.6.1.2.1.4.20.1.2.'+str(ip)
    print("OID: "+str(oid))
    index = consultaSNMP(comunidad, ip, oid)
    print("INDEX" +str(index))
    return  index