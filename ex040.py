from time import sleep
print('===EXERCÍCIO 040===')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('Analisando os valores...')
sleep(1)
if n1 > n2:
    print('O \033[1:33mprimeiro valor\033[m é maior.')
elif n2 > n1:
    print('O \033[1:33msegundo valor\033[m é maior')
elif n1 == n2:
    print('\033[1:33mNão existe valor maior\033[m, os dois valores são iguais.')
