#trabalho da matéria de LP - fazer um sistema bancario com orientação a objetos
#sistemaBancario 1.0-1
#a lógica do projeto. todas as funções estao funcionando aqui
#Os coxinhas: Cassius, Larissa e Robson

from conta import Conta
from pessoaJ import PessoaJ
from pessoaF import PessoaF
lista = []

def cadastro():
	print("Digite F,para pessoa física, e J, para pessoa Jurídica.")
	Tipoconta = input("Digite o tipo de conta que quer criar:\n")
	
	if Tipoconta == "F":
		cpf = int(input("Digite o seu CPF:\n"))
		nome = input("Digite seu nome:")
	elif Tipoconta == "J":
		cnpj = int(input("Digite o CNPJ da Empresa:\n"))
		razaos = input("Digite o nome da Empresa")

	tel = int(input("Digite o seu número de Telefone:\n"))
	endereco = input("Digite seu Endereço:\n") 

	if Tipoconta == "F":
		cliente = PessoaF(cpf, nome, tel, endereco)
	elif Tipoconta == "J":
		cliente = PessoaJ(cnpj, razaos, tel, endereco)
	
	lista.append(cliente)
	print("Cliente cadastrado com sucesso!")  
	pausar()    

def saque():
	saq = int(input("Qual é o número da conta para saque ?"))
	valor = float(input("Qual valor deseja sacar ?"))
	for conta in lista:
		if conta.getNumero() == saq:
			conta.sacar(valor)
			print("Transação realisada!")
			pausar()

def deposito():
	destino = int(input("Qual é o número da conta para depósito ?"))
	valor = float(input("Qual valor deseja depositar ?"))
	for conta in lista:
		if conta.getNumero() == destino:
			conta.depositar(valor)
			print("Transação realizada!")
			pausar()

def transferencia():
	valor = float(input("Qual o valor que deseja transferir? \n> R$ "))
	destino = int(input("Número da conta destino: \n> "))
	origem = int(input("Número da conta de origem: \n>"))
	for contaO in lista:
		if contaO.getNumero() == origem:
			for contaD in lista:
				if contaD.getNumero() == destino:
					contaO.transferir(valor, contaD)
					print("Operação realizada com sucesso!")
					pausar()

def extrato():
	ext = int(input("Digite o Número da sua Conta"))
	for conta in lista:
		if conta.getNumero() == ext:
			print(f"Seu Saldo é igual a {conta.getSaldo()}!")
			print("Esse é seu Histórico de Operação!")
			for item in conta.getExtrato():
				if item[0] == "Depósito":
					print(f" > Depósito de R$ {item[1]}")
				elif item[0] == "Saque":
					print(f" > Saque de R$ {item[1]}")
				elif item[0] == "Transferência para":
					print(f" > Transferência de R$ {item[1]} para {item[2]}")
				else: 
					print(f" > {item[2]} transferiu para você R$ {item[1]}")
			pausar()

			

def pausar():
	input("Aperte [ENTER] para continuar")

def menu():
	while True:
		print("""
		|   ^º^    BANCO DE J.P    ^º^     |
		|                                  |
		| 1- CADASTRAR                     |
		|                                  |
		| 2- SAQUE                         |
		|                                  |
		| 3- DEPÓSITO                      |
		|                                  |
		| 4- TRANSFERENCIA                 |
		|                                  | 
    	| 5- EXTRATO                       |          
		|                                  |        
		| 0- SAIR                          |
		|                                  | 
		""")

		print('Digite no teclado o número da opção q você deseja utilizar.\n')
		op = float(input("> "))
		
		if op == 1:
			cadastro()
		
		elif op == 2:
			saque()
		
		elif op == 3:
			deposito()
		
		elif op == 4:
			transferencia()
		
		elif op == 5:
			extrato()
		
		elif op == 0:
			print("Saindo...")
			break
		else:
			print("Opção Inválida")

menu()

  

