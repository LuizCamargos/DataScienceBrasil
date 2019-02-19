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
