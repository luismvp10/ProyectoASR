class Agente:
	def __init__(self, id1, index, hostName, snmpVersion, ipAgente, puerto, comunidad):
		self.id1=id1
		self.index = index
		self.hostName = hostName
		self.snmpVersion = snmpVersion
		self.ipAgente = ipAgente
		self.puerto = puerto
		self.comunidad = comunidad

	def ingresarHostName(Host):
		hostName = Host

	def ingresarSnmpVersion(version):
		snmpVersion = version

	def ingresarIp(ip):
		ipAgente = ip

	def ingresarPort(port):
		puerto = port

	def ingresarComunidad(community):
		comunidad = community

	def setId(id2):
		id1 = id2

	def getHostName(self):
		return self.hostName 

	def getSnmpVersion(self):
		return self.snmpVersion

	def getIp(self):
		return self.ipAgente

	def getPort(self):
		return self.puerto

	def getComunidad(self):
		return self.comunidad

	def getIndex(self):
		return self.index
	
	def getId(self):
		return self.id1


