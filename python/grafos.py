import datetime

t0 = datetime.datetime.now()

grafos = [[], [[], []]]

caminhosVerificados = []
menorTamanho = -1
caminhosVálidos = []


inputs = ['A', 'B', 5, 'S', 'A', 'C', 6, 'S', 'B', 'C', 5, 'S', 'B', 'D', 9, 'S', 'C', 'D', 8, 'N', 'A', 'D']
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
		print()
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
	print("-"*50)
	print("A menor distância percorrida é:  ", menorTamanho)
	print("O(s) melhor(es) caminho(s) é(são) esse(s):")
	for caminho in caminhosVálidos:
		print(" "*15+caminho)
	print("-"*50)
		
		
		
		
start()

t1 = datetime.datetime.now()
print(t1-t0)
	
