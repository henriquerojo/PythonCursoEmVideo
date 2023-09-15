print('===EXERCÍCIO 036===')
salário = float(input('Digite o salário do funcionário(a): R$'))
aumento = salário + (salário * 10 / 100)
if salário <= 1250:
    aumento = salário + (salário * 15 / 100)
print(f'O salário do funcionário(a) que era de \033[1:32mR${salário:.2f}\033[m passa a ser de \033[1:32mR${aumento:.2f}\033[m')
