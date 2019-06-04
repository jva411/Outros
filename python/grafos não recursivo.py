import datetime

t0 = datetime.datetime.now()

for i in range(0, 100000):
	pontos = [[], []]

	class ponto(object):
		def __init__(self, ponto):
			self.ponto = ponto
			self.chegadas = []
			self.chegadasD = []

	inputs = ['A', 'B', 5, 'S', 'A', 'C', 6, 'S', 'B', 'C', 5, 'S', 'B', 'D', 9, 'S', 'C', 'D', 8, 'S', 'C', 'E', 8,
			'S', 'E', 'G', 8, 'S', 'C', 'F', 8, 'S', 'F', 'G', 8, 'S', 'D', 'G', 8, 'S', 'C', 'H', 8, 'S', 'E', 'H', 8,
			'S', 'F', 'I', 8, 'S', 'E', 'I', 8, 'S', 'G', 'I', 8, 'S', 'F', 'H', 8, 'S', 'B', 'J', 8, 'S', 'A', 'E', 8,
			'S', 'G', 'K', 8, 'S', 'F', 'L', 8, 'S', 'E', 'K', 8, 'S', 'K', 'M', 8, 'S', 'L', 'N', 8, 'S', 'M', 'O', 8,
			'S', 'M', 'P', 8, 'S', 'M', 'Q', 8, 'S', 'N', 'R', 8, 'S', 'N', 'S', 8, 'S', 'N', 'T', 8, 'S', 'T', 'U', 8,
			'N', 'A', 'U']
	index = 0

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
		if not sair in pontos[0]:
			pontos[0].append(sair)
			pontos[1].append(ponto(sair))
		if not ate in pontos[0]:
			pontos[0].append(ate)
			pontos[1].append(ponto(ate))
		pSair = pontos[1][pontos[0].index(sair)]
		pAte = pontos[1][pontos[0].index(ate)]
		pAte.chegadas.append(sair+ate)
		pAte.chegadasD.append(d)
		for i in range(0, len(pSair.chegadas)):
			pAte.chegadas.append(pSair.chegadas[i]+ate)
			pAte.chegadasD.append(pSair.chegadasD[i]+d)
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

	# start = input("Digite o ponto de partida: ")
	start = inputs[index]
	index += 1
	# end = input("Digite o ponto objetivo: ")
	end = inputs[index]
	index += 1
	ponto = pontos[1][pontos[0].index(end)]
	menorDistancia = 0
	caminhosVálidos = [start]
	for i in range(0, len(ponto.chegadas)):
		caminho = ponto.chegadas[i]
		if caminho[0]==start:
			distancia = ponto.chegadasD[i]
			if menorDistancia==0 or distancia<menorDistancia:
				caminhosVálidos = [caminho]
				menorDistancia = distancia
			elif distancia==menorDistancia:
				caminhosVálidos.append(caminho)
	# print(menorDistancia)
	# print(caminhosVálidos)

t1 = datetime.datetime.now()

print(t1-t0)