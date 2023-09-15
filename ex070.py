from random import randint
cores = {'vermelhocomnegrito': '\033[1:31m',
         'limpa': '\033[m'}
while True:
    escolha = str(input('PAR OU ÍMPAR?[P/I]: ')).strip().upper()[0]
    if escolha not in 'P' and escolha not in 'I':
        print(f'{cores["vermelhocomnegrito"]}{"ERRO"}{cores["limpa"]}')
        break
    jogador = int(input('Escolha um número: '))
    computador = randint(0, 20)
    soma = computador + jogador
    print(f'O computador escolheu {computador}')
    print(f'{jogador} + {computador} = {soma}')
    if escolha in 'P' and soma % 2 == 0:
        print('PAR')
        print('JOGADOR VENCEU!')
    if escolha in 'I' and soma % 2 != 0:
        print('ÍMPAR')
        print('JOGADOR VENCEU!')
    if escolha in 'P' and soma % 2 != 0:
        print('ÍMPAR')
        print('COMPUTADOR VENCEU. VOCÊ PERDEU!')
        break
    if escolha in 'I' and soma % 2 == 0:
        print('PAR')
        print('COMPUTADOR VENCEU. VOCÊ PERDEU!')
        break
print('FIM')
