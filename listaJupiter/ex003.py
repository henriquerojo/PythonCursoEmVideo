#3. Escreva um programa que peça ao usuário para adivinhar um número secreto entre 1 e 100. O programa deve gerar aleatoriamente um
# número secreto e, em seguida, permitir que o usuário faça tentativas para adivinhá-lo. O programa deve fornecer dicas, dizendo se o
# número secreto é maior ou menor do que a tentativa atual. O programa deve continuar pedindo ao usuário para adivinhar até
# que ele acerte o número secreto. Quando o usuário acertar, o programa deve imprimir quantas tentativas foram necessárias.
# (Use random.randint() para gerar o número aleatório)
import random
contador = 1
numero = random.randint(1, 100)
while True:
    usuario = int(input('Digite um número inteiro entre 1 e 100: '))
    if usuario > numero:
        print('O número que você digitou é maior que o número sorteado, tente digitar um número menor')
    elif usuario < numero:
        print('O número que você digitou é menor que o número sorteado, tente digitar um número maior')
    else:
        print('Parabéns, você acertou o número.')
        break
    contador += 1
print(f'Foram necessárias {contador} tentativas para você adivinhar o número sorteado')
