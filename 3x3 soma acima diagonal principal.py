matriz = []

for l in range(3):
    linha = []
    for c in range(3):
        elemento = int(input("Digite um número na posição [%d][%d]: " %(l, c)))
        linha.append(elemento)

    matriz.append(linha)

for l in range (2):
    print(matriz[l])

soma = matriz[0][1]+matriz[0][2]+matriz[1][2]
print (soma)