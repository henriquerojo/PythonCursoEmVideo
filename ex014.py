print('===EXERCÍCIO 014===')
p = float(input('Qual o preço do produto?R$ '))
d = p*5/100
vp = p-d
print('O produto que custava \033[1:32mR${:.2f}\033[m, com o\033[33m desconto de 5%\033[m agora custa \033[1:32mR${:.2f}\033[m, com \033[1:32mR${:.2f}\033[m de desconto.'.format(p, vp, d))
