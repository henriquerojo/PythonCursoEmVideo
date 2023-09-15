"""co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa equivale a: {h:.2f}')"""
import math  # from math import hypot
print('===EXERCÍCIO 019===')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print(f'A hipotenusa equivale a: \033[4:32m{h:.3f}\033[m')
