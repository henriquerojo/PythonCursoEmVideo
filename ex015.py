print('===EXERCÍCIO 015===')
sa = float(input('Qual o salário do funcionário? R$'))
ns = sa + (sa * 15 / 100)
print('Com o\033[33m aumento de 15%\033[m o salário do funcionário que antes era de \033[1:32mR${:.2f}\033[m, passa a ser de \033[1:32mR${:.2f}\033[m'.format(sa, ns))
