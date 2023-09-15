from datetime import date
print('===EXERCÍCIO 41===')
ano_atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano
sexo = int(input("""Informe o seu sexo: 
[ 1 ] Masculino
[ 2 ] Feminino
Opção: """))
print(f'Você nasceu em {ano} e tem/terá {idade} ano(s) em {ano_atual}.')
if idade == 18 and sexo == 1:
    print('Você tem que se alistar IMEDIATAMENTE.')
elif idade < 18 and sexo == 1:
    saldo = 18 - idade
    ano_de_alistamento = ano_atual + saldo
    print(f'Você terá que se alistar daqui a {saldo} ano(s).')
    print(f'Seu ano de alistamento será o ano de {ano_de_alistamento}')
elif idade > 18 and sexo == 1:
    saldo = idade - 18
    ano_de_alistamento = ano_atual - saldo
    print(f'Já passou {saldo} ano(s) do alistamento.')
    print(f'Seu ano de alistamento foi o ano de {ano_de_alistamento}')
elif sexo == 2:
    print('Você não precisa se alistar no alistamento militar obrigatório, pois é só pra pessoas do sexo Masculino.')
