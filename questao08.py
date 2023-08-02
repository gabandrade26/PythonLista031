'''
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o valor do conbsumo médio do automóvel, quilômetros por litro.
'''

distancia = float(input("Poderia me informar qual será a distância percorrida, em quilômetros:"))
consumo = float(input("Qual é o consumo médio do automóvel?"))
conta = distancia / consumo
print("Esse é o quanto que você gastará de quantidade de litros:", conta)
