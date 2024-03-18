"""
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo.
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
"""
print ("Entre com os dados ")

num1 = int (input("Entre com um numero inteiro "))
num2 = int (input("Entre com um numero inteiro "))
num3 = float (input("Entre com um numero real "))

operacao1 = (num1 * 2) * (num2 / 2)
operacao2 = (num1 * 3) + num2
operacao3 = (num3 ** 3)


print ("Operação 1 " , operacao1)
print ("Operação 2 " , operacao2)
print ("Operação 3 " , operacao3)