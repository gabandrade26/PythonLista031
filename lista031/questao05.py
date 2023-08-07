'''
Fazer um programa que pergunte o salário de um funcionário e apresente este salário com um aumento de 15%.
'''

salario = float(input("Qual é o seu salário?"))
aumento = salario + (salario * 15/100)
print("Esse é o seu salário com o aumento proposto:", aumento)