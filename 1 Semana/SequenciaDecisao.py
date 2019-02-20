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
    Nota = [0, 0, 0]
    Nota.insert(0, int(input("\ndigite a primeira nota: ")))
    Nota.insert(1, int(input("\ndigite a segunda nota: ")))
    Nota.insert(2, (Nota[0]+Nota[1])/ 2)
    if Nota[2] == 10:
        print("Aprovado com Distincao")
    elif Nota[2] >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    print(Nota[2])
    