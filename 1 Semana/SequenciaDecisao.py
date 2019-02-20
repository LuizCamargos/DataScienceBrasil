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
    Nota5 = [0, 0, 0]
    Nota5.insert(0, int(input("\ndigite a primeira nota: ")))
    Nota5.insert(1, int(input("\ndigite a segunda nota: ")))
    Nota5.insert(2, (Nota5[0]+Nota5[1])/ 2)
    if Nota5[2] == 10:
        print("Aprovado com Distincao")
    elif Nota5[2] >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    print(Nota5[2])

elif entrada == 6:
    #6 Faça um Programa que leia três números e mostre o maior deles. 
    Num6 = [0, 0, 0]
    Num6[0] = float(input("\ndigite um numero: "))
    Num6[1] = float(input("\ndigite outro numero: "))
    Num6[2] = float(input("\ndigite mais um numero: "))
    if Num6[0] > Num6[1] and Num6[0] > Num6[2]:
        MaiorNumero6 = Num6[0]
    elif Num6[1] > Num6[0] and Num6[1] > Num6[2]:
        MaiorNumero6 = Num6[1]
    else:
        MaiorNumero6 = Num6[2]
    print("O maior numero e: "+str(MaiorNumero6))
elif entrada == 7:
    #7 Faça um Programa que leia três números e mostre o maior e o menor deles. 
    Num7 = [0, 0, 0]
    Num7[0] = float(input("\ndigite um numero: "))
    Num7[1] = float(input("\ndigite outro numero: "))
    Num7[2] = float(input("\ndigite mais um numero: "))
    if Num7[0] > Num7[1] and Num7[0] > Num7[2]:
        MaiorNumero7 = Num7[0]
        if Num7[1] < Num7[2]:
            MenorNumero7 = Num7[1]
        else:
            MenorNumero7 = Num7[2]
    elif Num7[1] > Num7[0] and Num7[1] > Num7[2]:
        MaiorNumero7 = Num7[1]
        if Num7[2] < Num7[0]:
            MenorNumero7 = Num7[2]
        else:
            MenorNumero7 = Num7[0]
    else:
        MaiorNumero7 = Num7[2]
        if Num7[1] < Num7[0]:
            MenorNumero7 = Num7[1]
        else:
            MenorNumero7 = Num7[0]
    print("O maior numero e: "+str(MaiorNumero7))
    print("O menor numero e: "+str(MenorNumero7))