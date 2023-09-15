print('===EXERCÍCIO 046===')
print(f'{" Lojas Guanabara ":=^90}')
valor = float(input('Digite o preço das compras:R$ '))
forma = int(input("""Informe a forma de pagamento:
[1] à vista dinheiro/cheque  
[2] à vista cartão crédito/débito
[3] 2x no cartão crédito/débito
[4] 3x ou mais no cartão crédito/débito
Opção: """))
# à vista dinheiro/cheque == 10% de desconto
# à vista cartão crédito/débito == 5% de desconto
# 2x no cartão crédito/débito == preço normal
# 3x ou mais no cartão crédito/débito == 20% de juros
if forma == 4:
    parcela = int(input('Em quantas parcelas será realizado o pagamento? '))
    juros = (valor * 20 / 100) + valor
    parcelas = juros / parcela
    print(f'O valor total foi R${juros:.2f} e você irá pagar {parcela} parcelas de R${parcelas:.2f} com 20% de juros.')
elif forma == 3:
    parcelas = valor / 2
    print(f'Sua compra foi parcelada em 2x e irá custar um total de R${valor:.2f}')
    print(f'Cada parcela será de R${parcelas:.2f}.')
elif forma == 2:
    desconto = valor - (valor * 5 / 100)
    print(f'Sua compra terá um total de 5% de desconto. De R${valor:.2f} para um valor total de R${desconto:.2f}.')
elif forma == 1:
    desconto = valor - (valor * 10 / 100)
    print(f'Sua compra terá um total de 10% de desconto. De R${valor:.2f} o valor total será de R${desconto:.2f}')
else:
    print('Opção inválida. Tente novamente!')
