print('===EXERCÍCIO 58===')
soma_idade = 0
maior_idade_homem = 0
menor_idade_homem = 0
maior_idade_mulher = 0
menor_idade_mulher = 0
nome_maior_idade_homem = ''
nome_menor_idade_homem = ''
nome_maior_idade_mulher = ''
nome_menor_idade_mulher = ''
contador_mulheres_menores_20_anos = 0
contador_homens_menores_20_anos = 0
for laço in range(1, 5):
    print(F'===== {laço}ª PESSOA =====')
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if laço == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        menor_idade_homem = idade
        nome_maior_idade_homem = nome
        nome_menor_idade_homem = nome
    elif idade > maior_idade_homem and sexo in 'Mm':
        maior_idade_homem = idade
        nome_maior_idade_homem = nome
    elif idade < menor_idade_homem and sexo in 'Mm':
        menor_idade_homem = idade
        nome_menor_idade_homem = nome
    elif laço == 1 and sexo in 'Ff':
        maior_idade_mulher = idade
        menor_idade_mulher = idade
        nome_maior_idade_mulher = nome
        nome_menor_idade_mulher = nome
    elif idade > maior_idade_mulher and sexo in 'Ff':
        maior_idade_mulher = idade
        nome_maior_idade_mulher = nome
    elif idade < menor_idade_mulher and sexo in 'Ff':
        menor_idade_mulher = idade
        nome_menor_idade_mulher = nome
    if sexo in 'Mm' and idade < 20:
        contador_homens_menores_20_anos += 1
    if sexo in 'Ff' and idade < 20:
        contador_mulheres_menores_20_anos += 1
media = soma_idade / 4
print(f'A média de idade dessas 4 pessoas é de {media:.1f} ano(s)')
print(f'O homem com a MAIOR idade é o {nome_maior_idade_homem} e ele possui {maior_idade_homem} ano(s) de idade!')
print(f'O homem com a MENOR idade é o {nome_menor_idade_homem} e ele possui {menor_idade_homem} ano(s) de idade!')
print(f'A mulher com a MAIOR idade é a {nome_maior_idade_mulher} e ela possui {maior_idade_mulher} ano(s) de idade!')
print(f'A mulher com a MENOR idade é a {nome_menor_idade_mulher} e ela possui {menor_idade_mulher} ano(s) de idade!')
print(f'São/É {contador_homens_menores_20_anos} homens menor(es) de 20 ano(s) de idade!')
print(f'São/É {contador_mulheres_menores_20_anos} mulher(es) menor(es) de 20 ano(s) de idade!')
