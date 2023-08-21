matriz = []

for l in range(2):
    linha = []
    for c in range(2):
        elemento = int(input("Digite um número na posição [%d][%d]: " %(l, c)))
        linha.append(elemento)

    matriz.append(linha)

for l in range (2):
    print(matriz[l])

determinante = matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
print (determinante)