vazar = 0

while vazar != 1:
    print("------------------------------------------------------------------------")
    print("\t Calculadora de Matrizes \t")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Sair")

    dig = int(input("Digite a opção desejada: "))

    if dig == 1:
        matriz1 = []
        som = []
        for i in range(3):
            linha = []
            for j in range(3):
                elemento = int(input("Digite um número na posição [%d][%d]: " %(i, j)))
                linha.append(elemento)

            matriz1.append(linha)

        matriz2 = []
        for i in range(3):
            linha = []
            for j in range(3):
                elemento = int(input("Digite um número na posição [%d][%d]:" %(i, j)))
                linha.append(elemento)

            matriz2.append(linha)

        for i in range(3):
            linha = []
            for j in range(3):
                soma = matriz1[i][j] + matriz2[i][j]
                linha.append(soma)
            som.append(linha)
                
        print("------------")
        print("SOMA:")
        for l in range(3):
            print(som[l])

    elif dig == 2:
        matriz1 = []
        sub = []

        for i in range(3):
            linha = []
            for j in range(3):
                elemento = int(input("Digite um número na posição [%d][%d]:" %(i, j)))
                linha.append(elemento)

            matriz1.append(linha)

        matriz2 = []
        for i in range(3):
            linha = []
            for j in range(3):
                elemento = int(input("Digite um número na posição [%d][%d]:" %(i, j)))
                linha.append(elemento)

            matriz2.append(linha)

        for i in range(3):
            linha = []
            for j in range(3):
                subtração = matriz1[i][j] - matriz2[i][j]
                linha.append(subtração)
            sub.append(linha)
                
        print("------------")
        print("Subtração:")
        for l in range(3):
            print(sub[l])
    
    elif dig == 3:
        matriz1 = []
        mult = []

        for i in range(3):
            linha = []
            for j in range(3):
                elemento = int(input("Digite um número na posição [%d][%d]:" %(i, j)))
                linha.append(elemento)

            matriz1.append(linha)

        matriz2 = []
        for i in range(3):
            linha = []
            for j in range(3):
                elemento = int(input("Digite um número na posição [%d][%d]:" %(i, j)))
                linha.append(elemento)

            matriz2.append(linha)

        for i in range(3):
            linha = []
            for j in range(3):
                multiplicação = 0
                for k in range(3):
                    multiplicação += matriz1[i][k] * matriz2[k][j]
                linha.append(multiplicação)
            mult.append(linha)

        print("------------")
        print("Multiplicação:")
        for l in range(3):
            print(mult[l])

    elif dig == 4:
        print("Se retirando da Calculadora de Matrizes...")
    else:
        print("Digite uma opção válida!")
        break