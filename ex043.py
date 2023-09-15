from datetime import date
print('===EXERCÍCIO 043===')
ano = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Você pertence a categoria MIRIM.')
elif idade <= 14:
    print('Você pertence a categoria INFANTIL.')
elif idade <= 19:
    print('Você pertence a categoria JUNIOR.')
elif idade <= 25:
    print('Você pertence a categoria SÊNIOR.')
elif idade >= 25:
    print('Você pertence a categoria MASTER.')
