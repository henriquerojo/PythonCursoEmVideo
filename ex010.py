print('===EXERCÍCIO 010===')
n = float(input('Você possui quantos metros de altura? '))
cm = n * 100
mm = n * 1000
texto = {'ciano': '\033[36m',
         'negrito': '\033[1:33m',
         'limpa': '\033[m'}
print(f'Sua altura em centímetros é {texto["ciano"]}{cm}{texto["limpa"]}cm, e em milímetros é {texto["ciano"]}{mm}{texto["limpa"]}mm')
n1 = float(input('Digite uma medida em metros: '))
km = n1 / 1000
hm = n1 / 100
dam = n1 / 10
dm = n1 * 10
centimetros = n1 * 100
milimetros = n1 * 1000
print(f'A medida de {texto["negrito"]}{n1}{texto["limpa"]}m, corresponde a: \n{texto["ciano"]}{km}{texto["limpa"]}km; \n{texto["ciano"]}{hm}{texto["limpa"]}hm; \n{texto["ciano"]}{dam}{texto["limpa"]}dam; \n{texto["ciano"]}{dm}{texto["limpa"]}dm; \n{texto["ciano"]}{centimetros}{texto["limpa"]}cm; \n{texto["ciano"]}{milimetros}{texto["limpa"]}mm;')
