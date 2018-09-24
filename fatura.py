def main():
	nome = input("Digite o nome do cliente: ")
	diaVencimento = input("Digite o dia de vencimento: ")
	mesVencimento = input("Digite o mês de vencimento: ")
	valorFatura = input("Digite o valor da fatura: ")
	print("Olá, %s\nA sua fatura com vencimento em %s de %s no valor de R$%s está fechada." %(nome, diaVencimento, mesVencimento, valorFatura))

main()