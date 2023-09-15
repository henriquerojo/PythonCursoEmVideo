print('===EXERCÍCIO 017===')
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos quilômetros rodados? '))
pagamento = dias * 60 + km * 0.15
print('O aluguel do veículo custará \033[1:32mR${:.2f}\033[m'.format(pagamento))
