from datetime import date
print('===EXERCÍCIO 056===')
atual = date.today().year
total_maior = 0
total_menor = 0
for data in range(1, 8):
    nascimento = int(input(f'Em qual ano nasceu à {data}ª pessoa? '))
    idade = atual - nascimento
    if idade >= 18:
        total_maior += 1
    elif idade < 18:
        total_menor += 1
print(f'Há um total de {total_maior} pessoa(as) maiores de idade.')
print(f'Há um total de {total_menor} pessoa(as) menores de idade.')
