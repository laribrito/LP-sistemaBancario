#Documento para a classe conta, que abriga 
#atributos comuns entre as classes de cliente


class Conta:
	__numeroLivre = 1011
	def __init__(self, tel, endereco): 
		self.__numero = Conta.__numeroLivre
		Conta.__numeroLivre += 1
		self.__tel = tel
		self.__endereco = endereco
		self.__saldo = 0
		self.__extrato = []
		
	def getSaldo(self):
		return self.__saldo
	
	def getNumero(self):
		return self.__numero
		
	def getEndereco(self):
		return self.__endereco
		
	def getTel(self):
		return self.__tel
		
	def getExtrato(self):
		return self.__extrato

	def sacar(self, valor):
		if valor <= 0:
			return 1    # Código de erro pra valor negativo
		elif valor > self.__saldo:
				return 2    # Código de erro pra saldo insuficiente
		else:
			self.__saldo -= valor
			saque = ["Saque", valor]
			self.__extrato.append(saque)
			return 0    # Código de erro pra sucesso
				

	def depositar(self, valor):
		if valor > 0:
			self.__saldo += valor
			deposito = ["Depósito", valor]
			self.__extrato.append(deposito)
			return 0  # Código de erro pra sucesso
		else:
			return 1 # Código de erro pra valor negativo
		
	def transferir(self, valor, destino):
		#retiro o valor da conta atual
		if valor <= 0:
			return 1    # Código de erro pra valor negativo
		elif valor > self.__saldo:
			return 2    # Código de erro pra saldo insuficiente
		else:
			self.__saldo -= valor
			#deposito na conta destino
			destino.__saldo += valor

			transferencia = ["Transferência para", valor, destino.getNumero()]
			self.__extrato.append(transferencia)
			transferencia = ["Transferência de", valor, self.getNumero()]
			destino.__extrato.append(transferencia)
			return 0  # Código de erro pra sucesso

