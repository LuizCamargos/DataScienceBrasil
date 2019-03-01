import math
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
elif entrada == 9:
    #9 Faça um Programa que leia três números e mostre-os em ordem decrescente.
    ListaNum9 = []
    for i in range(0, 3):
        num9 = float(input("Digite um numero: "))
        ListaNum9.append(num9)
    ListaOrdenada9 = sorted(ListaNum9, reverse = True)
    print(ListaOrdenada9)
elif entrada == 10:
    #10 Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
    horario10 = input("\ndigite M-matutino ou V-Vespertino ou N- Noturno: ")
    if horario10 == "M":
        print("\nBom dia!")
    elif horario10 == "V":
        print("\nBoa tarde!")
    elif horario10 == "N":
        print("\nBoa Noite!")
    else:
        print("Valor Invalido!")
elif entrada == 11:
    #Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    #salários até R$ 280,00 (incluindo) : aumento de 20%
    #salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    #salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    #salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    #o salário antes do reajuste;
    #o percentual de aumento aplicado;
    #o valor do aumento;
    #o novo salário, após o aumento.
    salario11 = float(input("\nDigite seu salario: "))
    if salario11 <= 280.0:
        taxa11 = salario11*0.2
        porcentual11 = 20
    elif salario11 <= 700.0:
        taxa11 = salario11*0.15
        porcentual11 = 15
    elif salario11 <= 1500.0:
        taxa11 = salario11*0.1
        porcentual11 = 10
    else:
        taxa11 = salario11 * 0.05
        porcentual11 = 5
    total11 = salario11 + taxa11
    print("salario R${0}, com ajuste : R${1}".format(salario11, total11))
    print("porcentual aplicado: {0}%, valor porcentual: R${1}\n".format(porcentual11, taxa11))
elif entrada == 12:
    #12 Faça um programa para o cálculo de uma folha de pagamento
    salariohora12 = round(float(input("\nDigite seu salario/hora: ")), 2)
    horastrabalhadas12 = round(float(input("\nDigite suas horas de trabalho do mes: ")), 2)
    salariobruto12 =  round(salariohora12 * horastrabalhadas12, 2)
    FGTS12 = round(salariobruto12 * 0.11, 2)
    INSS12 = round(salariobruto12 * 0.1, 2)
    if salariobruto12 <= 900.0:
        IR12 = 0
    elif salariobruto12 <= 1500.0:
        IR12 = 0.05
    elif salariobruto12 <= 2500:
        IR12 = 0.12
    else:
        IR12 = 0.2
    IR12 = round(salariobruto12 * IR12, 2)
    salarioLiq12 = salariobruto12 - (IR12 + FGTS12)
    print("salario Bruto    :R$ "+str(salariobruto12))
    print("IR               :R$ "+str(IR12))
    print("INSS             :R$ "+str(INSS12))
    print("FGTS             :R$ "+str(FGTS12))
    print("Total descontos  :R$ "+str(salariobruto12 - salarioLiq12))
    print("Salario Liquido  :R$ "+str(salarioLiq12))
elif entrada == 13:
    #13 Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
    diaDaSemana13 = int(input("Digite um dia dia semana (1-Domingo...):"))
    ListaDias13 = ["Invalido","Domingo","Segunda","Terca","Quarta","Quinta","Sexta","Sabado"]
    try:
        print(ListaDias13[diaDaSemana13])
    except :
        print("Valor invalido!")
elif entrada == 14:
    #14 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
    nota14 = 0
    conceito14 = "E"
    aprovados14 = ["A","B","C"]
    for i in range(2):
        nota14 += int(input("Digite uma nota: "))
    nota14 /= 2

    if nota14 > 9.0:
        conceito14 = "A"
    elif nota14 > 7.5:
        conceito14 = "B"
    elif nota14 > 6.0:
        conceito14 = "C"
    elif nota14 > 4.0:
        conceito14 = "D"
    
    print("Nota: {0}, Conceito: {1}".format(nota14,conceito14))
    if conceito14 in aprovados14:
        print("Apovado")
    else:
        print("Reprovado")
elif entrada == 15:
    #15 Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.  
    lados15 = input("Digite os tres lados do triangulo(dando espaco): ").split(" ")
    ladoA15 = lados15.count(lados15[0])
    ladoB15 = lados15.count(lados15[1])

    if ladoA15 == 3:
        print("Triangulo Equilatero")
    elif ladoA15 and ladoB15 == 1:
        print("Triangulo Escaleno")
    elif ladoA15 or ladoB15 == 2:
        print("Triangulo Isosceles")
    else:
        print("digite corretamente")
    print(ladoA15, ladoB15)

elif entrada == 16:
    #16 Faça um programa que calcule as raízes de uma equação do segundo grau
    a16, b16, c16 = list(map(int, input("Digite os valores A, B e C(dando espaco): ").split(" ")))
    delta16 = b16**2 -4 *a16 *c16
    if delta16 < 0:
        print("Delta negativo")
    elif delta16 == 0:
        print("delta = 0")
    else:
        Xa16 = (-b16 + math.sqrt(delta16))/ (2 * a16)
        Xb16 = (-b16 - math.sqrt(delta16))/ (2 * a16)
        print("Equacao de 2 grau: ",Xa16, "\t", Xb16)
    print(delta16)

elif entrada == 17:
    #17 Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
    ano17 = int(input("Digite um ano para saber se e ou nao bissexto: "))
    anobissexto17 = False
    if ano17 % 4 == 0:
        if ano17 % 100 != 0:
            anobissexto17 = True
        elif ano17 % 100 == 0:
            if ano17 % 400 == 0:
                anobissexto17 = True

    if anobissexto17 == True:
        print("Ano bissexto!")
    else:
        print("Nao e ano bissexto")

elif entrada == 18:
    #18 Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
    dd18, mm18, aaaa18 = list(map(int , (input("Digite uma data no formato dd/mm/aaaa: ").split("/"))))
    listaMeses31dias18 = [1,3,5,7,8,10,12]
    anobissexto18 = False
    valido = True

    if aaaa18 % 4 == 0:
        if aaaa18 % 100 != 0:
            anobissexto18 = True
        elif aaaa18 % 100 == 0:
            if aaaa18 % 400 == 0:
                anobissexto18 = True

    if dd18 > 31 or dd18 < 1 or mm18 < 1 or mm18 > 12 or aaaa18 < 1:
        valido = False
    if dd18 != 31 and mm18 not in listaMeses31dias18:
        valido = False
    if anobissexto18 == True and mm18 == 2 and dd18 < 30 :
        valido = True

    print(valido)