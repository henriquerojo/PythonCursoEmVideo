from time import sleep
print('===EXERCÍCIO 037===')
print('==--==--' * 20)
print('Me diga a medida de três retas e eu te falo se é possível formar um triângulo com essas medidas.')
print('--==--==' * 20)
medida1 = float(input('Digite a medida da primeira reta em centímetros (cm): '))
medida2 = float(input('Digite a medida da segunda reta em centímetros (cm): '))
medida3 = float(input('Digite a medida da terceira reta em centímetros (cm): '))
print('Aguarde um instante...')
sleep(3)
if medida1 + medida2 > medida3 and medida2 + medida3 > medida1 and medida1 + medida3 > medida2:
    print('Com essas medidas \033[1:32mé possível\033[m formar um triângulo.')
else:
    print('Com essas medidas \033[1:31mNÃO é possível\033[m formar um triângulo.')
