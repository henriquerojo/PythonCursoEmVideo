print('===EXERCÍCIO 012===')
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real/4.91
euro = real/5.85
libra = real/6.83
print('Com \033[1:32mR${:.2f}\033[m reais, você pode comprar \033[1:32mUS${:.2f}\033[m dólares'.format(real, dolar))
print('Com \033[1:32mR${:.2f}\033[m reais, você pode comprar \033[1:32m€${:.2f}\033[m euros'.format(real, euro))
print('Com \033[1:32mR${:.2f}\033[m reais, você pode comprar \033[1:32m£${:.2f}\033[m libras esterlinas'.format(real, libra))
