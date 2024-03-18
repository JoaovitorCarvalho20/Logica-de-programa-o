"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
print ("Entre com os dados pedidos ")

horasvalor= float(input("Entre com o valor da sua hora de serviço "))
horasTrabalhadas = float(input("Entre com a quantidade de horas trabalhadas no mes "))

salario = horasvalor*horasTrabalhadas

print("Seu salario nesse mes e = ", salario )