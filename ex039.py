print('===EXERCÍCIO 039===')
número = int(input('Digite um valor inteiro: '))
print('''Escolha uma das bases para conversão
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{número} convertido para BINÁRIO é {bin(número)[2:]}')
elif opção == 2:
    print(f'{número} convertido para OCTAL é {oct(número)[2:]}')
elif opção == 3:
    print(f'{número} convertido para HEXADECIMAL é {hex(número)[2:]}')
else:
    print('Opção inválida. Tente novamente!')
