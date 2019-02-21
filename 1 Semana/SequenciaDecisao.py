entrada = int(input("Digite o numero da questao: "))

if entrada == 1:
    #1 Faça um Programa que peça dois números e imprima o maior deles.
    numA1 = float(input("\nDigite um numero : "))
    numB1 = float(input("Digite outro numero : "))
    if numA1 > numB1:
        print("o maior numero e: "+str(numA1))
    else:
        print("o maior numero e: "+str(numB1))
elif entrada == 2:
    #2 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
    num2 = float(input("\nDigite um numero : "))
    if num2 > 0:
        print("numero positivo")
    else:
        print("numero negativo")
elif entrada == 3:
    #3 Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
    sexo3 = input("\nDigite  : F - Feminino ou M - Masculino: ")
    if sexo3 == "F":
        print("Feminino")
    elif sexo3 == "M":
        print("Masculino")
    else:
        print("sexo invalido!")
elif entrada == 4:
    #4 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
    vogais4 = "AEIOU"
    letra4 = input("\ndigite uma letra: ")
    letra4 = letra4.upper()
    if letra4 in vogais4:
        print("e Vogal")
    else:
        print("nao e volgal")
elif entrada == 5:
    #5 Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: 
        #A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
        #A mensagem "Reprovado", se a média for menor do que sete; 
        #A mensagem "Aprovado com Distinção", se a média for igual a dez. 
    ac = 0
    for i in range(0, 2):
        ac += float(input("\ndigite uma nota: "))
    ac/=2
    if ac == 10:
        print("Aprovado com Distincao")
    elif ac >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    print(ac)
elif entrada == 6:
    #6 Faça um Programa que leia três números e mostre o maior deles. 
    ListaNum6 = []
    for i in range(0, 3):
        num6 = float(input("Digite um numero: "))
        ListaNum6.append(num6)
    ListaOrdenada6 = sorted(ListaNum6)
    print("O maior numero e: "+str(ListaOrdenada6[2]))
elif entrada == 7:
    #7 Faça um Programa que leia três números e mostre o maior e o menor deles. 
    ListaNum7 = []
    for i in range(0, 3):
        num7 = float(input("Digite um numero: "))
        ListaNum7.append(num7)
    ListaOrdenada7 = sorted(ListaNum7)
    print("O maior numero e: "+str(ListaOrdenada7[2]))
    print("O menor numero e: "+str(ListaOrdenada7[0]))
elif entrada == 8:
    #8 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 
    ProdutoA8 = float(input("\ndigite o preco do produto A: "))
    ProdutoB8 = float(input("\ndigite o preco do produto B: "))
    ProdutoC8 = float(input("\ndigite o preco do produto C: "))
    if ProdutoA8 < ProdutoB8 and ProdutoA8 < ProdutoC8:
        print("\nProduto A vale mais a pena")
    elif ProdutoB8 < ProdutoA8 and ProdutoB8 < ProdutoC8:
        print("\nProduto B vale mais a pena")
    else:
        print("\nProduto C vale mais a pena")