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
    nota = []
    notaSoma =0 
    for i in range(1, 5):
        nota.append(float(input("\n digite a nota {0}: ".format(i))))
        notaSoma += nota[(i-1)]
    notaSoma /= 4
    print("\n nota final: {0}".format(notaSoma))
        
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
    farenheit = float(input("\ntemperatura em farenheit: "))
    Celsius = (farenheit - 32) / 1.8
    print("\ntemperatura em celsius: {0}".format(Celsius))

elif entrada == 10:
    #10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
    Celsius = float(input("\ntemperatura em celsius: "))
    farenheit = (Celsius * 1.8) + 32
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
else:
    print("error")

time.sleep(3)
