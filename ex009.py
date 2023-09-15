print('===EXERCÍCIO 009===')
texto = {'amarelo': '\033[33m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'limpa': '\033[m'}
n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))
m = float((n1+n2)/2)
if m > 6:
    print(f'A nota {texto["amarelo"]}média{texto["limpa"]} entre as duas provas desse aluno(a) é: {texto["azul"]}{m}{texto["limpa"]}')
if m == 6:
    print(
        f'A nota {texto["amarelo"]}média{texto["limpa"]} entre as duas provas desse aluno(a) é: {texto["verde"]}{m}{texto["limpa"]}')
if m < 6:
    print(
        f'A nota {texto["amarelo"]}média{texto["limpa"]} entre as duas provas desse aluno(a) é: {texto["vermelho"]}{m}{texto["limpa"]}')
