from time import sleep
from random import randint
print('===EXERCÍCIO 047===')
opção = int(input("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
O que você escolhe? """))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
computador = randint(0, 2)  # número gerado randomicamente pelo computador
if opção == 0 and computador == 0:  # você escolheu PEDRA e o computador jogou PEDRA
    print('==--==--' * 5)
    print('Você jogou PEDRA e o computador jogou PEDRA!')
    print('\033[1:33mEMPATAMOS!\033[m')
    print('--==--==' * 5)
elif opção == 0 and computador == 1:  # você escolheu PEDRA e o computador jogou PAPEL
    print('==--==--' * 5)
    print('Você jogou PEDRA e o computador jogou PAPEL!')
    print('\033[1:31mVOCÊ PERDEU!\033[m')
    print('--==--==' * 5)
elif opção == 0 and computador == 2:  # você escolheu PEDRA e o computador jogou TESOURA
    print('==--==--' * 5)
    print('Você jogou PEDRA e o computador jogou TESOURA!')
    print('\033[1:32mVOCÊ GANHOU!\033[m')
    print('--==--==' * 5)
elif opção == 1 and computador == 0:  # você escolheu PAPEL e o computador jogou PEDRA
    print('==--==--' * 5)
    print('Você jogou PAPEL e o computador jogou PEDRA!')
    print('\033[1:32mVOCÊ GANHOU!\033[m')
    print('--==--==' * 5)
elif opção == 1 and computador == 1:  # você escolheu PAPEL e o computador jogou PAPEL
    print('==--==--' * 5)
    print('Você jogou PAPEL e o computador jogou PAPEL!')
    print('\033[1:33mEMPATAMOS!\033[m')
    print('--==--==' * 5)
elif opção == 1 and computador == 2:  # você escolheu PAPEL e o computador jogou TESOURA
    print('==--==--' * 5)
    print('Você jogou PAPEL e o computador jogou TESOURA!')
    print('\033[1:31mVOCÊ PERDEU!\033[m')
    print('--==--==' * 5)
elif opção == 2 and computador == 0:  # você escolheu TESOURA e o computador jogou PEDRA
    print('==--==--' * 5)
    print('Você jogou TESOURA e o computador jogou PEDRA!')
    print('\033[1:31mVOCÊ PERDEU!\033[m')
    print('--==--==' * 5)
elif opção == 2 and computador == 1:  # você escolheu TESOURA e o computador JOGOU PAPEL
    print('==--==--' * 5)
    print('Você jogou TESOURA e o computador jogou PAPEL!')
    print('\033[1:32mVOCÊ GANHOU!\033[m')
    print('--==--==' * 5)
elif opção == 2 and computador == 2:  # você escolheu TESOURA e o computador jogou TESOURA
    print('==--==--' * 5)
    print('Você jogou TESOURA e o computador jogou TESOURA!')
    print('\033[1:33mEMPATAMOS!\033[m')
    print('--==--==' * 5)
else:  # quando o usuário escolhe uma opção que não pode ser PEDRA, PAPEL OU TESOURA.
    print('Opção inválida. Tente novamente!')
