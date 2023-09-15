print('===EXERCÍCIO 027===')
nome = str(input('Digite seu nome completo: ')).strip().title()
print(f'Seu nome possui Souza? \033[31m{"Souza" in nome}\033[m')
print(f'Seu nome é \033[33m{nome}\033[m')
