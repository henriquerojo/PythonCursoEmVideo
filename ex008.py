print('===EXERCÍCIO 008===')
n1 = int(input('Digite um número: '))
d = n1*2
t = n1*3
rq = n1**(1/2)
print('Analisando o valor {}{}{} \nSeu dobro é {}{}{}. \nSeu triplo é {}{}{}. \nE sua raiz quadrada é {}{:.3f}{}.'.format('\033[32m', n1, '\033[m', '\033[35m', d, '\033[m', '\033[35m', t, '\033[m', '\033[35m', rq, '\033[m'))
