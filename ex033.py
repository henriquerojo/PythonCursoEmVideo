print('===EXERCÍCIO 033===')
distância = float(input('Digite a distância em quilômetros (km): '))
viagens_de_até_200km = 0.50 * distância
viagens_acima_de_200km = 0.45 * distância
print(f'Você está prestes a começar uma viagem de \033[33m{distância}\033[m km')
if distância > 200:
    print(f'O preço da passagem será de \033[32mR${viagens_acima_de_200km:.2f}\033[m')
else:
    print(f'O preço da passagem será de \033[32mR${viagens_de_até_200km:.2f}\033[m')
