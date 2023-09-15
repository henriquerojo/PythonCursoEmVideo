from time import sleep
print('===EXERCÍCIO 006===')
texto = {'amarelo': '\033[33m',
         'azul': '\033[34m',
         'limpa': '\033[m'}  # cores para os textos de pergunta
resposta = {'verdecomfundobrancoemnegrito': '\033[1:32:107m'}  # cor para a resposta do is
print('')
um = input('\033[4mDigite algo:\033[m ')  # interação com o usuário
print('Aguarde...')
sleep(2)  # tempo de 2 segundos de espera usando a biblioteca time com o módulo sleep
print('')  # espaço
print('Você digitou: ''\033[1m''"', um, '"''\033[m')  # mostrando o que o usuário digitou
print('')  # espaço
print(f'{texto["amarelo"]}O tipo primitivo desse valor é: {texto["limpa"]}{resposta["verdecomfundobrancoemnegrito"]}{type(um)}{texto["limpa"]}')
print(f'{texto["azul"]}É um valor numérico?{texto["limpa"]}{resposta["verdecomfundobrancoemnegrito"]}{um.isnumeric()}{texto["limpa"]}')
print(f'{texto["azul"]}É um valor alfabético?{texto["limpa"]}{resposta["verdecomfundobrancoemnegrito"]}{um.isalpha()}{texto["limpa"]}')
print(f'{texto["azul"]}É um valor alfanumérico?{texto["limpa"]}{resposta["verdecomfundobrancoemnegrito"]}{um.isalnum()}{texto["limpa"]}')
print(f'{texto["azul"]}Só tem espaços?{texto["limpa"]}{resposta["verdecomfundobrancoemnegrito"]}{um.isspace()}{texto["limpa"]}')
print(f'{texto["azul"]}Está somente em maiúsculas?{texto["limpa"]}{resposta["verdecomfundobrancoemnegrito"]}{um.isupper()}{texto["limpa"]}')
print(f'{texto["azul"]}Está somente em minúsculas?{texto["limpa"]}{resposta["verdecomfundobrancoemnegrito"]}{um.islower()}{texto["limpa"]}')
print(f'{texto["azul"]}Está capitalizada?{texto["limpa"]}{resposta["verdecomfundobrancoemnegrito"]}{um.istitle()}{texto["limpa"]}')
print('')
dois = input('\033[4mDigite aleatoriamente:\033[m ')  # interação com o usuário
print('Aguarde...')
sleep(2)  # tempo de 2 segundos de espera usando a biblioteca time com o módulo sleep
print('')  # espaço
print('Você digitou: ''\033[1m''"', dois, '"''\033[m')
print('')  # espaço
print('{}O tipo primitivo de {} é: {}{}{}{}'.format(texto["amarelo"], dois, texto["limpa"], resposta["verdecomfundobrancoemnegrito"], type(dois), texto["limpa"]))
print('{}{} é numérico?{} {}{}{}'.format(texto["azul"], dois, texto["limpa"], resposta['verdecomfundobrancoemnegrito'], dois.isnumeric(), texto["limpa"]))
print('{}{} é alfabético?{} {}{}{}'.format(texto["azul"], dois, texto["limpa"], resposta["verdecomfundobrancoemnegrito"], dois.isalpha(), texto["limpa"]))
print('{}{} é alfanumérico?{} {}{}{}'.format(texto["azul"], dois, texto["limpa"], resposta["verdecomfundobrancoemnegrito"], dois.isalnum(), texto["limpa"]))
print('{}{} só tem espaços?{} {}{}{}' .format(texto["azul"], dois, texto["limpa"], resposta["verdecomfundobrancoemnegrito"], dois.isspace(), texto["limpa"]))
print('{}{} está somente em letras maiúsculas?{} {}{}{}'.format(texto["azul"], dois, texto["limpa"], resposta["verdecomfundobrancoemnegrito"], dois.isupper(), texto["limpa"]))
print('{}{} está somente em letras minúsculas?{} {}{}{}'.format(texto["azul"], dois, texto["limpa"], resposta["verdecomfundobrancoemnegrito"], dois.islower(), texto["limpa"]))
print('{}{} está capitalizado?{} {}{}{}'.format(texto["azul"], dois, texto["limpa"], resposta["verdecomfundobrancoemnegrito"], dois.istitle(), texto["limpa"]))
