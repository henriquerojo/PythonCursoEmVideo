print('===EXERCÍCIO 013===')
L = float(input('Largura da parede(em metros): '))
H = float(input('Altura da parede(em metros): '))
A = L*H
texto = {'vermelho': '\033[31m',
         'negrito': '\033[1m',
         'pretoebranco': '\033[7m',
         'limpa': '\033[m'}
print(f'As dimensões da sua parede são:{texto["negrito"]}{L}{texto["limpa"]}{texto["vermelho"]}m{texto["limpa"]}x{texto["negrito"]}{H}{texto["limpa"]}{texto["vermelho"]}m{texto["limpa"]}, ocupando uma área de {texto["pretoebranco"]}{A}{texto["limpa"]}{texto["vermelho"]}m²{texto["limpa"]}.')
T = A/2
print(f'A quantidade de tinta necessária para pintar sua parede é em torno de {texto["pretoebranco"]}{T}{texto["limpa"]}{texto["vermelho"]}l{texto["limpa"]}.')
