from math import pi
import time

entrada = int(input("digite um numero da lista de exercicios: "))

if entrada == 1:
    #1 Faca um Programa que mostre a mensagem "Alo mundo" na tela.
    print("\n alo mundo")

elif entrada == 2:
    #2 Faca um Programa que peca um numero e então mostre a mensagem O número informado foi [numero].
    num2 = int(input("\n digite um numero: "))
    print(" O número informado foi: {0}".format(num2))

elif entrada == 3:
    #3 Faca um Programa que peca dois numeros e imprima a soma.)
    num3A = int(input("\n digite um numero: "))
    num3B = int(input("\n digite um numero: "))
    num3C = num3A + num3B
    print(num3C)

elif entrada == 4:
    #4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
    nota4 = []
    notaSoma4 =0
    for i in range(1, 5):
        nota4.append(float(input("\n digite a nota {0}: ".format(i))))
        notaSoma4 += nota4[(i-1)]
    notaSoma4 /= 4
    print("\n nota final: {0}".format(notaSoma4))

elif entrada == 5:
    #5 Faça um Programa que converta metros para centímetros.
    m5 = float(input("\n conversor metros para centimetros: "))
    cm5 = m5 * 100
    print("\n{0} centimetros.".format(cm5))

elif entrada == 6:
    #6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
    r6 = float(input("\n digite o raio do circulo: "))
    A6 = pi * (r6**2)
    print("\na area do circulo e: {0}".format(A6))

elif entrada == 7:
    #7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
    l7 = float(input("\n digite um lado do quadrado: "))
    R7 = (l7 * l7) * 2
    print("\no dobro da area do quadradoe: {0}".format(R7))

elif entrada == 8:
    #8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
    salario8 = float(input("\nsalario por hora: "))
    horas8 = float(input("\nhoras trabalhadas: "))
    print("\nsalario deste mes: {0}".format((salario8*horas8)))

elif entrada == 9:
    #9 Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
    farenheit9 = float(input("\ntemperatura em farenheit: "))
    Celsius9 = (farenheit9 - 32) / 1.8
    print("\ntemperatura em celsius: {0}".format(Celsius9))

elif entrada == 10:
    #10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
    Celsius10 = float(input("\ntemperatura em celsius: "))
    farenheit = (Celsius10 * 1.8) + 32
    print("\ntemperatura em farenheit: {0}".format(farenheit))
elif entrada == 11:
    #11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # A) o produto do dobro do primeiro com metade do segundo.
    # B) a soma do triplo do primeiro com o terceiro.
    # C) o terceiro elevado ao cubo.
    num11A = int(input("\ndigite um numero int: "))
    num11B = int(input("\ndigite outro numero int: "))
    num11C = float(input("\ndigite um numero float: "))
    print(num11A * 2 + num11B / 2)
    print(num11A * 3 + num11C)
    print(num11C ** 3)

elif entrada == 12:
    #Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
    altura12 = float(input("\ndigite sua altura em metros: "))
    pesoIdeal12 = (72.7*altura12) - 58
    print("\nseu peso ideal e: {0}".format(pesoIdeal12))

elif entrada == 13:
    #Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    # A)Para homens: (72.7*h) - 58
    # B)Para mulheres: (62.1*h) - 44.7
    altura13 = float(input("\ndigite sua altura em metros: "))
    sexo13 =  int(input("\ndigite 1 para homem e 0 para mulher: "))
    if sexo13 == 1:
        pesoIdeal13 = (72.7*altura13) - 58
    else:
        pesoIdeal13 = (62.1*altura13) - 44.7

    print("\nseu peso ideal e: {0}".format(pesoIdeal13))
elif entrada == 14:
    #faça um programa que leia a variável peso (peso de peixes) e calcule o excesso, mostre o excesso(se +50kg) e o valor da multa
    peso14 = float(input("\ndigite o peso de pexes: "))
    excesso14 = peso14 - 50
    multa14 = 0
    if excesso14 > 0:
        multa14 = excesso14 * 4.0
    print("multa: {0}, excesso: {1}".format(multa14,excesso14))
elif entrada == 15:
    #Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salario15 = float(input("\nsalario por hora: "))
    horas15 = float(input("\nhoras trabalhadas: "))
    SalBruto15 = salario15 * horas15
    INSS15 = SalBruto15 * 0.08
    IR15 = SalBruto15 * 0.11
    sindicato15 = SalBruto15 * 0.05

    SalLiquido = SalBruto15 - ( sindicato15 + INSS15 + IR15)
    print("\n+ Salário Bruto : R$"+str(SalBruto15))
    print("\n- IR (11%) : R$"+str(IR15))
    print("\n- INSS (8%) : R$"+str(INSS15))
    print("\n- Sindicato ( 5%) : R$"+str(sindicato15))
    print("\n= Salário Liquido : R$"+str(SalLiquido))

elif entrada == 16:
    #16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
    # Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
    # Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
    areaQuadrada16 = float(input("\ndigite a area quadrada: "))
    tinta16 = areaQuadrada16 / 3
    latasTinta16 = round(tinta16 + 0.5, 0)
    custo16 = latasTinta16 * 80
    print("\nLatas necessarias: {0}, Custo: R${1}".format(latasTinta16, custo16))
elif entrada == 17:
    #Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    #Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    # A) comprar apenas latas de 18 litros;
    # B) comprar apenas galões de 3,6 litros;
    # C) misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
    areaQuadrada17 = float(input("\ntamanho da area m²: "))
    litros17 = areaQuadrada17 / 6
    latasTinta17 = round((litros17 / 18)+0.5 , 0)
    valorLatas17 = latasTinta17 * 80.0
    galoesTinta17 = round((litros17 / 3.6 )+0.5, 0)
    valorGaloes17 = galoesTinta17 * 25.0
    sobra17 = round(((litros17 % 18)/3.6) + 0.5, 0)
    valorMisto = sobra17 * 25.0 + valorLatas17
    print("latas de 18 litros: R$" + str(valorLatas17))
    print("galões de 3,6 litros: R$" + str(valorGaloes17))
    print("misto + 10%: R$"+str(valorMisto))
elif entrada == 18:
    #Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
    # calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
    tamanho18 = float(input("\ndigite o tamanho do arquivo em MB: "))
    velocidade18 = float(input("\ndigite a velocidade da coneccao em Mbps: "))
    tempo18 = (tamanho18 / velocidade18)
    print("ETA: "+str(tempo18)+" min")
else:
    print("error")

time.sleep(1)
