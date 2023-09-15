from random import randint
cores = {'vermelho': '\033[31m',
         'verde': '\033[32m',
         'limpa': '\033[m'}
sorteio = randint(0, 20)
contador = 0
print('===EXERCÍCIO 060===')
print('==--' * 20)
print('Vou pensar em um número entre 0 e 20, tente adivinhar!')
print('--==' * 20)
numero = int(input('Digite um valor entre 0 e 20: '))
while numero != sorteio:
    if numero != sorteio:
        print(f'{cores["vermelho"]}ERROU{cores["limpa"]}')
        numero = int(input('Digite novamente: '))
        contador += 1
print(f'{cores["verde"]}PARABÉNS VOCÊ ACERTOU!{cores["limpa"]}, foi necessário {contador + 1} tentativa(s) para acertar o número!')
