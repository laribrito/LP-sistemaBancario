# coding: utf-8
#trabalho da matéria de LP - fazer um sistema bancario com orientação a objetos
#sistemaBancario 1.0-2 
#implementar o uso do limite de crédito nas contas
#Os coxinhas: Cassius🤡, Larissa😎 e Robson🙃

from pessoaJ import PessoaJ
from pessoaF import PessoaF

import os
lista = []


def cadastro():
	limpar()
	print("Cadastro!")
	print("Digite:\n [F] - Para pessoa Física. \n [J] - Para pessoa Jurídica.")
	Tipoconta = input("Digite o tipo de conta que quer criar:\n > ")
	limpar()

	if Tipoconta.lower() == "f":
		print("Pessoa Física!")
		cpf = int(input("Digite o seu CPF:\n > "))
		nome = input("Digite seu nome:\n > ")
	elif Tipoconta.lower() == "j":
		print("Pessoa Jurídica!")
		cnpj = int(input("Digite o CNPJ da Empresa:\n > "))
		razaos = input("Digite o nome da Empresa: \n > ")

	tel = int(input("Digite o seu número de Telefone:\n > "))
	endereco = input("Digite seu Endereço:\n > ") 

	if Tipoconta.lower() == "f":
		cliente = PessoaF(cpf, nome, tel, endereco)
	elif Tipoconta.lower() == "j":
		cliente = PessoaJ(cnpj, razaos, tel, endereco)
	
	print(f"\nO Número da sua conta é: {cliente.getNumero()}")
	print(f"Você tem R$ {(-1)*cliente.getLimite()} de Crédito Especial!")
	lista.append(cliente)
	print("\nCliente cadastrado com sucesso!")  
	pausar()
	limpar()

def saque():
	limpar()
	print("Saque!")
	#recebe o numero da conta
	saq = int(input("Qual é o número da conta para saque ?\n > "))
	#procura na lista
	nEncontrou = True
	for conta in lista:
		if conta.getNumero() == saq:
			nEncontrou = False
			conta.testarLimite()
			print(f"\nSeu saldo atual é: R$ {conta.getSaldo()}")
			print(f"Você tem  R$ {(-1)*conta.getLimite()} de Crédito Especial!\n")
			#pergunta o valor que quer sacar
			valor = float(input("Qual valor deseja sacar ?\n> R$ "))
			tst = conta.sacar(valor)
			#recebe e testa o código de erro
			if tst == 1:
				print("Você digitou um valor negativo. Tente novamente!")
			elif tst == 2:
				print("Você não tem saldo suficiente. Tente novamente!")
			elif tst == 3:
				print("Você não tem saldo suficiente e não quis usar o crédito especial!")
			else: 
				print("Transação realizada!")
			pausar()
			limpar()
	if nEncontrou:
		print("Conta não encontrada. Tente novamente!")
		pausar()
		limpar()
	
def deposito():
	limpar()
	print("Depósito!")
	#recebe o numero da conta destino e o valor do deposito
	destino = int(input("Qual é o número da conta para depósito? \n > "))
	#procura na lista
	nEncontrou = True
	for conta in lista:
		if conta.getNumero() == destino:
			nEncontrou = False
			conta.testarLimite()
			#se encontrar a conta, pede o valor
			valor = float(input("Qual valor deseja depositar ?\n > R$ "))
			tst = conta.depositar(valor)
			#recebe e testa o código de erro
			if tst == 1:
				print("Você digitou um valor negativo. Tente novamente!")
			else:
				print("Transação realizada!")
			pausar()
			limpar()
	if nEncontrou:
		print("Conta não encontrada. Tente novamente!")
		pausar()
		limpar()

def transferencia():
	limpar()
	print("Tranferência")
	#recebe o numero da conta origem
	origem = int(input("Número da conta de origem: \n > "))
	#busca a conta de origem na lista
	nEncontrouO = True
	nEncontrouD = True
	for contaO in lista:
		if contaO.getNumero() == origem:
			nEncontrouO = False
			contaO.testarLimite()
			print(f"\nSeu saldo atual é de: R$ {contaO.getSaldo()}")
			print(f"Você tem  R$ {(-1)*contaO.getLimite()} de Crédito Especial!\n")
			valor = float(input("Qual o valor que deseja transferir? \n > R$ "))
			#recebe conta destino
			destino = int(input("Número da conta destino: \n > "))
			#busca a conta de destino na lista
			for contaD in lista:
				if contaD.getNumero() == destino:
					nEncontrouD = False
					#efetua a tranferencia
					tst = contaO.transferir(valor, contaD)
					#recebe e testa o código de erro
					if tst == 1:
						print("Você digitou um valor negativo. Tente novamente!")
					elif tst == 2:
						print("Você não tem saldo suficiente. Tente novamente!")
					elif tst == 3:
						print("Você não tem saldo suficiente e não quis usar o crédito especial!")
					else:
						print("Transação realizada!")
					pausar()
					limpar()
					
	if nEncontrouO:
		print("Conta de origem não encontrada. Tente novamente!")
		pausar()
		limpar()
	elif nEncontrouD:
		print("Conta destino não encontrada. Tente novamente!")
		pausar()
		limpar()
		
def extrato():
	limpar()
	print("Extrato!")
	ext = int(input("Digite o Número da sua Conta:\n > "))
	nEncontrou = True
	for conta in lista:
		if conta.getNumero() == ext:
			nEncontrou = False
			conta.testarLimite()
			print(f"\nSeu Saldo é igual a R$ {conta.getSaldo()}!")
			print(f"Você tem R$ {(-1)*conta.getLimite()} de Crédito Especial!\n")
			print("Esse é seu Histórico de Operação!")
			if len(conta.getExtrato()) == 0:
					print("     ----------------------")
			else:
				for item in conta.getExtrato():
					if item[0] == "Depósito":
						print(f" - Depósito de R$ {item[1]}")
					elif item[0] == "Saque":
						print(f" - Saque de R$ {item[1]}")
					elif item[0] == "Transferência para":
						print(f" - Transferência de R$ {item[1]} para {item[2]}")
					else: 
						print(f" - {item[2]} transferiu para você R$ {item[1]}")
			pausar()
			limpar()
	if nEncontrou:
		print("Conta destino não encontrada. Tente novamente!")
		pausar()
		limpar()

			

def pausar():
	input("Aperte [ENTER] para continuar\n")

def limpar():
	try:
		os.system('clear')
	except TypeError:
		os.system('cls')

def menu():
	while True:
		limpar()
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

		print('Digite no teclado o número da opção que você deseja utilizar.\n')
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
