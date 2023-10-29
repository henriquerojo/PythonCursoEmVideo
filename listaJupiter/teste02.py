#Utilize a mesma lógica do enunciado anterior, mas, agora diga se o aluno passou de ano ou não passou ou se ficou de recuperação.
# SE a nota for maior que 5 e menor que 7, o aluno ficou de recuperação.
# Se ele tirou 7 ou mais, ele passou de ano. Caso contrário ele repetiu.
# Exiba isso na tela dependendo da nota MÉDIA do aluno.

# recebendo as notas
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

#calculando a média
media = (n1 + n2) / 2

#definindo estrutura condicional
if media > 5 and media < 7: # se a media for MAIOR que 5 e MENOR que 7, ele retorna 'Recuperação'
    print('Recuperação')
elif media >= 7: # se a media for 7 ou mais, ele retorna 'Aprovado'
    print('Aprovado')
else: # se ele não tiver de recuperação nem for aprovado, ele só pode retornar 'Reprovado'
    print('Reprovado')
