#trabalho da matéria de LP - fazer um sistema bancario com orientação a objetos
#sistemaBancario 1.0-1
#padronizar os prints e inputs, fazendo um trabalho estético
#Os coxinhas: Cassius, Larissa e Robson

from conta import Conta
from pessoaJ import PessoaJ
from pessoaF import PessoaF
import os
lista = []


def cadastro():
	limpar()
	print("Digite:\n [F] - Para pessoa Física. \n [J] - Para pessoa Jurídica.")
	Tipoconta = input("Digite o tipo de conta que quer criar:\n > ")
	limpar()

	if Tipoconta.lower() == "f":
		print("Pessoa Física!")
		cpf = int(input("Digite o seu CPF:\n > "))
		nome = input("Digite seu nome:\n > ")
	elif Tipoconta.lower() == "j":
		print("Pessoa Jurídica!")
		cnpj = int(input("Digite o CNPJ da Empresa:\n >"))
		razaos = input("Digite o nome da Empresa: \n > ")

	tel = int(input("Digite o seu número de Telefone:\n > "))
	endereco = input("Digite seu Endereço:\n > ") 

	if Tipoconta.lower() == "f":
		cliente = PessoaF(cpf, nome, tel, endereco)
	elif Tipoconta.lower() == "j":
		cliente = PessoaJ(cnpj, razaos, tel, endereco)
	print(f"\nO Número da sua conta é: {cliente.getNumero()}")
	lista.append(cliente)
	print("\nCliente cadastrado com sucesso!")  
	pausar()
	limpar()

def saque():
	limpar()
	print("Saque!")
	saq = int(input("Qual é o número da conta para saque ?\n >"))
	for conta in lista:
		if conta.getNumero() == saq:
			print(f"Seu saldo atual é: R$ {conta.getSaldo()}")
			valor = float(input("Qual valor deseja sacar ?\n> R$ "))
			conta.sacar(valor)
			print("Transação realizada!")
			pausar()
			limpar()

def deposito():
	limpar()
	print("Depósito!")
	destino = int(input("Qual é o número da conta para depósito? \n > "))
	valor = float(input("Qual valor deseja depositar ?\n > R$ "))
	for conta in lista:
		if conta.getNumero() == destino:
			conta.depositar(valor)
			print("Transação realizada!")
			pausar()
			limpar()

def transferencia():
	limpar()
	print("Tranferência")
	valor = float(input("Qual o valor que deseja transferir? \n > R$ "))
	origem = int(input("Número da conta de origem: \n > "))
	#busca a conta de origem na lista
	for contaO in lista:
		if contaO.getNumero() == origem:
			print(f"Seu saldo atual é de: R$ {contaO.getSaldo()}")
			destino = int(input("Número da conta destino: \n > "))
			#busca a conta de destino
			for contaD in lista:
				if contaD.getNumero() == destino:
					#efetua a tranferencia
					contaO.transferir(valor, contaD)
					print("Transação realizada!")
					pausar()
					limpar()

def extrato():
	limpar()
	print("Extrato!")
	ext = int(input("Digite o Número da sua Conta: "))
	for conta in lista:
		if conta.getNumero() == ext:
			print(f"Seu Saldo é igual a R$ {conta.getSaldo()}!")
			print("Esse é seu Histórico de Operação!")
			if len(conta.getExtrato()) == 0:
					print("     ----------------------")
			else:
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
			limpar()

			

def pausar():
	input("Aperte [ENTER] para continuar")

def limpar():
	try:
		os.system('clear')
	except TypeError:
		os.system('cls')

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

  

