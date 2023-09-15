print('===EXERCÍCIO 038===')
print('Vamos realizar um empréstimo para sua compra do imóvel')
preço = float(input('Digite o preço do imóvel: R$'))
salário = float(input('Digite o seu salário atual: R$'))
tempo = int(input('Em quantos anos você precisa para pagar o empréstimo?  '))
valor_da_parcela = salário * 30 / 100
meses = tempo * 12
custo = preço / meses
if custo > valor_da_parcela:
    print(f'Você \033[31mNÃO poderá\033[m realizar este empréstimo. Pois para pagar uma casa de R${preço:.2f} em {tempo} anos, o valor da parcela ultrapassará 30% da sua renda. \nO valor da parcela será de R${custo:.2f}.')
else:
    print(f'Você \033[36mpoderá\033[m realizar este financiamento. Pois para pagar uma casa de R${preço:.2f} em {tempo} anos, o valor da parcela é inferior a 30% da sua renda. \nCada parcela custará R${custo:.2f}.')
