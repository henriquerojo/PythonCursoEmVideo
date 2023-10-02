#4. Crie um dicionário que represente um catálogo de produtos. Cada chave do dicionário deve ser o nome de um produto e o valor deve ser o
# preço desse produto. Em seguida, escreva um programa que solicite ao usuário que insira o nome de um produto e, em seguida,
# imprima o preço desse produto. Se o produto não estiver no catálogo, o programa deve informar que o produto não está disponível.
produtos = {
    'carne': 30.99,
    'leite': 5.00,
    'arroz': 22.00,
    'feijao': 10.99,
}
nome = str(input('Digite o nome de um produto: '))
if nome in produtos:
    print(f'O preço de {nome} é de {produtos[nome]:.2f}')
else:
    print('O produto não está disponível')
