'''
Fazer um programa que pergunte uma temperatura ao usuário, em graus Fahrenheit, e apresente esta temperatura convertida em graus Celsius. A fórmula da conversão é c=(f-32)*5:9, onde c é a temperatura em graus Celsius e f em Fahrenheit.
'''

f = float(input("Poderia me informar uma temperatura em Fahrenheit:"))
c = (f - 32) * 5 / 9
print("Essa é a temperatura em Celsius:", c)