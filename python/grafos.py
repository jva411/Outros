grafos = [] # [[A][[B, C],[10, 15]]]

grafos.append(["A"])
grafos.append([[["B"]], [[10]]]) #[["A"], [[["B", "C"], ["C"]], [10, 15]] ]
grafos[1][0][0].append("C")
grafos[1][1][0].append(22)
grafos[0].append("B")
grafos[1][0].append(["C"])
grafos[1][1].append([7])

caminhosVerificados = []
menorTamanho = 0
caminhosVálidos = []

def recursão(start, end, tamanho, caminho, index):
    global caminhosVerificados
    global menorTamanho
    global caminhosVálidos
    n = grafos[0].index(start)
    if n==len(grafos[1][0]) or end==start:
        if caminho in caminhosVerificados:
            return caminho[:-1]
        if tamanho<menorTamanho or menorTamanho==0:
            caminhosVálidos = [caminho]
            menorTamanho = tamanho
        elif tamanho==menorTamanho:
            caminhosVálidos.append(caminho)
        caminhosVerificados.append(caminho)
        return caminho
    now = grafos[1][0][n][index]
    caminho += now
    tamanho += grafos[1][1][n][index]
    caminho2 = recursão(now, end, tamanho, caminho, index)
    if caminho2==caminho:
        recursão(now, end, tamanho, caminho, index+1)

recursão("A", "C", 0, "", 0)

print(menorTamanho, caminhosVálidos, "\n\n", caminhosVerificados)

print(grafos)