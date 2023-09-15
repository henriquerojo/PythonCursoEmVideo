print('==EXERCÍCIO 044===')
medida1 = float(input('Primeiro segmento: '))
medida2 = float(input('Segundo segmento: '))
medida3 = float(input('Terceiro segmento: '))
if medida1 + medida2 > medida3 and medida1 + medida3 > medida2 and medida2 + medida3 > medida1 == medida2 != medida3 or medida1 == medida3 != medida2 or medida2 == medida3 != medida1:
    print('Essas medidas \033[1:32mPODEM FORMAR\033[m um triângulo ISÓSCELES.')
elif medida1 + medida2 > medida3 and medida1 + medida3 > medida2 and medida2 + medida3 > medida1 == medida2 == medida3:
    print('Essas medidas \033[1:32mPODEM FORMAR\033[m um triângulo EQUILÁTERO.')
elif medida1 + medida2 > medida3 and medida1 + medida3 > medida2 and medida2 + medida3 > medida1 != medida2 != medida3:
    print('Essas medidas \033[1:32mPODEM FORMAR\033[m um triângulo ESCALENO.')
else:
    print('Essas medidas \033[1:31mNÃO PODEM FORMAR\033[m um triângulo.')
