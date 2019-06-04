import datetime

t0 = datetime.datetime.now()

for ind in range(0, 100000):
	grafos = [[], [[], []]]

	caminhosVerificados = []
	menorTamanho = -1
	caminhosVálidos = []


	inputs = ['A', 'B', 5, 'S', 'A', 'C', 6, 'S', 'B', 'C', 5, 'S', 'B', 'D', 9, 'S', 'C', 'D', 8, 'S', 'C', 'E', 8,
			'S', 'E', 'G', 8, 'S', 'C', 'F', 8, 'S', 'F', 'G', 8, 'S', 'D', 'G', 8, 'S', 'C', 'H', 8, 'S', 'E', 'H', 8,
			'S', 'F', 'I', 8, 'S', 'E', 'I', 8, 'S', 'G', 'I', 8, 'S', 'F', 'H', 8, 'S', 'B', 'J', 8, 'S', 'A', 'E', 8,
			'S', 'G', 'K', 8, 'S', 'F', 'L', 8, 'S', 'E', 'K', 8, 'S', 'K', 'M', 8, 'S', 'L', 'N', 8, 'S', 'M', 'O', 8,
			'S', 'M', 'P', 8, 'S', 'M', 'Q', 8, 'S', 'N', 'R', 8, 'S', 'N', 'S', 8, 'S', 'N', 'T', 8, 'S', 'T', 'U', 8,
			'N', 'A', 'U']
	index = 0

	def menorCaminho(start, end, distancia, caminho):
		global menorTamanho
		global caminhosVálidos
		if start==end:
			caminhosVerificados.append(caminho)
			if distancia < menorTamanho or menorTamanho==-1:
				menorTamanho = distancia
				caminhosVálidos = [caminho]
			elif distancia==menorTamanho:
				caminhosVálidos.append(caminho)
		else:
			n = grafos[0].index(start)
			for i in range(0, len(grafos[1][0][n])):
				menorCaminho(grafos[1][0][n][i], end, distancia + grafos[1][1][n][i], caminho + grafos[1][0][n][i])

	def start():
		global inputs
		global index
		while True:
			# sair = input("Digite o ponto de partida: ")
			sair = inputs[index]
			index += 1
			# ate = input("Digite o ponto de chegada: ")
			ate = inputs[index]
			index += 1
			# d = int(input("Digite a distancia: "))
			d = inputs[index]
			index += 1
			if not sair in grafos[0]:
				grafos[0].append(sair)
				grafos[1][0].append([ate])
				grafos[1][1].append([d])
			else:
				n = grafos[0].index(sair)
				if ate in grafos[1][0][n]:	
					grafos[1][1][n][grafos[1][0][n].index(ate)] = d
				else:
					grafos[1][0][n].append(ate)
					grafos[1][1][n].append(d)
			if not ate in grafos[0]:
				grafos[0].append(ate)
				grafos[1][0].append([])
				grafos[1][1].append([])
			# print()
			# option = input("Deseja adicionar outro ponto? (S/N)\n").lower()
			option = inputs[index].lower()
			index += 1
			while not(option=='s' or option=='n'):
				print("Opção inválida!")
				print()
				option = input("Deseja adicionar outro ponto? (S/N)\n").lower()
			if option=='n':
				break 
		start = inputs[index]
		index += 1
		# end = input("Digite o ponto objetivo: ")
		end = inputs[index]
		index += 1
		menorCaminho(start, end, 0, start)
		# print("-"*50)
		# print("A menor distância percorrida é:  ", menorTamanho)
		# print("O(s) melhor(es) caminho(s) é(são) esse(s):")
		# for caminho in caminhosVálidos:
		# 	print(" "*15+caminho)
		# print("-"*50)
			
			
			
			
	start()


print("-"*50)
print("A menor distância percorrida é:  ", menorTamanho)
print("O(s) melhor(es) caminho(s) é(são) esse(s):")
for caminho in caminhosVálidos:
	print(" "*15+caminho)
print("-"*50)


t1 = datetime.datetime.now()
print(t1-t0)

	
