'''
Fazer um algoritmo que afetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação=valor+(valor*(taxa/100)*tempo em dias)
'''

valor = float(input("Qual o valor da prestação?"))
dias = float(input("Quantos dias a prestação está atrasada?"))
taxa = float(input("Qual a taxa da prestação?"))
prestacao = valor + (valor * (taxa / 100) * dias)
print("Esse é o valor da prestação em atraso:", prestacao)