print('===EXERCÍCIO 045===')
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / altura ** 2
print(f'Seu índice de massa corporal (IMC) é {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc == 18.5 or imc < 25:
    print('Você está com o peso ideal.')
elif imc == 25 or imc < 30:
    print('Você está com sobrepeso.')
elif imc == 30 or imc < 40:
    print('Você está com obesidade.')
elif imc > 40:
    print('Você está com obesidade mórbida, cuidado!')
