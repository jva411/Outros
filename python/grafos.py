grafos = [[], [[], []]]

caminhosVerificados = []
menorTamanho = 0
caminhosVálidos = []

def recursão(start, end, tamanho, caminho, index, zera):
    global caminhosVerificados
    global menorTamanho
    global caminhosVálidos
    Lcaminho = caminho
    Ltamanho = tamanho
    Lindex = index
    if zera:
        Lindex = 0
    n = grafos[0].index(start)
    if n==len(grafos[1][0]) or end==start or Lindex>=len(grafos[1][0][n]):
        if not end==start:
            return [Lcaminho[:-1], False]
        if Lcaminho in caminhosVerificados:
            return [Lcaminho[:-1], False]
        if Ltamanho<menorTamanho or menorTamanho==0:
            caminhosVálidos = [Lcaminho]
            menorTamanho = Ltamanho
        elif Ltamanho==menorTamanho:
            caminhosVálidos.append(Lcaminho)
        caminhosVerificados.append(Lcaminho)
        return [Lcaminho, True]
    now = grafos[1][0][n][Lindex]
    Lcaminho += now
    Ltamanho += grafos[1][1][n][Lindex]
    caminho2 = recursão(now, end, Ltamanho, Lcaminho, Lindex, True)
    Lindex += 1
    while (not caminho2[1]) and Lindex<len(grafos[1][0][n]):
        Ltamanho -= grafos[1][1][n][Lindex-1]
        caminho2 = recursão(start, end, Ltamanho, Lcaminho[:-1], Lindex, False)
        Lindex += 1
    return caminho2

def menorCaminho(start, end):
    for i in range(0, len(grafos[1][0])):
        for i2 in range(0, len(grafos[1][0][i])):
            recursão(start, end, 0, start, 0, False)
            print("-"*50)


def start():
	while True:
		sair = input("Digite o ponto de partida: ")
		ate = input("Digite o ponto de chegada: ")
		d = int(input("Digite a distancia: "))
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
		option = input("Deseja adicionar outro ponto? (S/N)\n").lower()
		while not(option=='s' or option=='n'):
			print("Opção inválida!")
			print()
			option = input("Deseja adicionar outro ponto? (S/N)\n").lower()
		if option=='n':
			break
	start = input("Digite o ponto de partida: ")
	end = input("Digite o ponto objetivo: ")
	menorCaminho(start, end)
	print("-"*50)
	print("A menor distância percorrida é:  ", menorTamanho)
	print("O(s) melhor(es) caminho(s) é(são) esse(s):")
	print("-"*50)
	for caminho in caminhosVálidos:
		print(" "*15+caminho)
		
		
		
		
start()
	
