print('===EXERCÍCIO 42===')
nota1 = float(input('Digite a primeira nota do aluno(a): '))
nota2 = float(input('Digite a segunda nota do aluno(a): '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Sua média foi {media:.1f}.')
    print('Sua nota foi \033[36mabaixo\033[m da nossa média. Portanto você está \033[1:31mREPROVADO\033[m!')
elif media > 6.9:
    print(f'Sua média foi {media:.1f}')
    print(f'Sua nota foi \033[36macima\033[m da nossa média. Portanto você está \033[1:32mAPROVADO\033[m!')
else:
    print(f'Sua média foi {media:.1f}')
    print(f'Sua nota foi \033[36mregular\033[m. Portanto você está de \033[1:33mRECUPERAÇÃO\033[m!')
