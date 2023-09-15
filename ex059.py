print('===EXERCÍCIO 059===')
sexo = str(input('Informe seu sexo [M/F]: ')).upper()[0].strip()  # Não precisa do [0], pode causar erros
while sexo != 'M' and sexo != 'F':  # not in 'MF'
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).upper()[0].strip()
print(f'Sexo {sexo} registrado com sucesso!')
