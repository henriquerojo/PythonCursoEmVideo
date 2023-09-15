from math import sin, cos, tan, radians  # import math
print('===EXERCÍCIO 020===')
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
print(f'O ângulo \033[35m{angulo}\033[m tem o seno igual a: \033[35m{seno:.2f}\033[m')
cosseno = cos(radians(angulo))
print(f'O ângulo \033[35m{angulo}\033[m tem o cosseno igual a: \033[35m{cosseno:.2f}\033[m')
tg = tan(radians(angulo))
print(f'O ângulo \033[35m{angulo}\033[m tem a tangente igual a: \033[35m{tg:.2f}\033[m')
