matriz = []

for l in range(3):
    linha = []
    for c in range(3):
        elemento = int(input("Digite um número na posição [%d][%d]: " %(l, c)))
        linha.append(elemento)

    matriz.append(linha)

for l in range (3):
    print(matriz[l])

print("--------------------------")

matrizt = []
for l in range(3):
    linhat = []
    for c in range(3):
        linhat.append(matriz[c][l])
    matrizt.append(linhat)

for l in range(3):
    print(matrizt[l])