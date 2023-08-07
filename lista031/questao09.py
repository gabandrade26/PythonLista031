'''
Fazer um algoritmo que pergunte 1 número e apresente: a) o próprio número/ b) O quadrado deste número/ c) A raiz quadrada deste número.
'''
import math

num = float(input("Me informe um número:"))
potencia = math.pow(num,2)
raiz = math.sqrt(num)
print("Aqui o seu número informado", num, ",o quadrado dele", potencia, "e a sua raiz", raiz)
