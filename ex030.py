from random import randint  # import random
from time import sleep  # import time
print('===EXERCÍCIO 030===')
print('\033[33m==--==--==\033[m' * 20)
print('\033[34mEu pensei em um número entre 0 e 10\033[m')
print('\033[33m--==--==--\033[m'*20)
n = int(input('\033[34mEm que número eu pensei? \033[m'))  # interação com o usuário
r = randint(0, 10)  # número gerado randomicamente pelo computador
print('\033[1:37mAguarde...\033[m')
sleep(3)  # simulação de loading
print(f'Eu pensei no número {r}')
if n == r:
    print('\033[1:32mPARABÉNS! Você ganhou!\033[m')
    print('\033[1:32m--FIM--\033[m')
else:
    print('\033[1:31mVOCÊ PERDEU!\033[m\033[0:37m Dessa vez eu ganhei, quem sabe na próxima...\033[m')
    print('\033[1:31m--FIM--\033[m')
