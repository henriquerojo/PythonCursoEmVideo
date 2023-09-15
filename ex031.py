print('===EXERCÍCIO 031===')
velocidade = float(input('Qual é a velocidade atual do carro em km/h? '))
pagamento = (velocidade - 80) * 7
if velocidade > 80:
    print(f'\033[1:31mVocê foi multado(a)\033[m em \033[32mR${pagamento:.2f}\033[m, por ultrapassar o limite de velocidade de 80 km/h.')
print('\033[33mTenha um bom dia e dirija com responsabilidade!\033[m')
