from time import sleep
from datetime import date
print('===EXERCÍCIO 034===')
ano = int(input('Digite o ano e descubra se ele foi/será um ano bissexto ou digite 0 para saber o ano atual: '))
print('\033[33mAguarde...\033[m')
sleep(2)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[36m{ano}\033[m\033[1:37m foi/será um ano bissexto.\033[m')
else:
    print(f'\033[36m{ano}\033[m\033[1:37m não foi ou não será um ano bissexto.\033[m')
"""print(f'{ano} foi ou será um ano bissexto' if ano % 4 == 0 else print(f'{ano} não foi ou não será um ano bissexto'))"""
