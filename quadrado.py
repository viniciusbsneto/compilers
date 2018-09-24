def main():
	lado = float(input("Digite o valor correspondente ao lado de um quadrado: "))
	area = lado ** 2
	perimetro = 4 * lado
	print("perímetro: %.2f - área: %.2f" %(perimetro, area))
	
main()