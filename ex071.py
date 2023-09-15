from time import sleep
print('===EXERCÍCIO 071===')
cores = {'amarelo': '\033[33m',
         'limpa': '\033[m'}
pergunta = ''
contador_homens = contador_maiordeidade = contador_mulher = 0
while True:
    print('-' * 30)
    print(f'{"CADASTRO":^30}')
    print('-' * 30)
    idade = int(input('Informe sua idade: '))
    if idade >= 18:
        contador_maiordeidade += 1
    sexo = str(input('Informe seu sexo entre Masculino ou Feminino [M/F]: ')).upper()[0].strip()
    while sexo not in 'Mm' and sexo not in 'Ff':
        sexo = str(input('Informe seu sexo entre Masculino ou Feminino [M/F]: ')).upper()[0].strip()
    if sexo in 'Mm':
        contador_homens += 1
    if sexo in 'Ff' and idade < 20:
        contador_mulher += 1
    pergunta = str(input('Quer continuar? [S/N]: ')).upper()[0].strip()
    while pergunta not in 'Ss' and pergunta not in 'Nn':
        pergunta = str(input('Quer continuar? [S/N]: '))
    if pergunta in 'Nn':
        break
print('Processando...')
sleep(1)
print(f'Foi registrado {cores["amarelo"]}{contador_maiordeidade}{cores["limpa"]} pessoa(s) maior(es) de idade!')
print(f'Foi registrado {cores["amarelo"]}{contador_homens}{cores["limpa"]} homens.')
print(f'Foi registrado {cores["amarelo"]}{contador_mulher}{cores["limpa"]} mulher(es) menor(es) de 20 anos.')
