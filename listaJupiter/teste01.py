#Você não é economia? Agora vamo mexer com números...
# Solicite ao usuário digitar o salário dele. Pensa em que tipo de dado um salário é armazenado,é float, int?
# Mas pensa isso em TODAS as questões, isso é importante.
# Independente do salário digitado pelo usuário, faça um cálculo para aumentar o salário dele em 10% e exiba na tela.

salario = float(input('Digite o seu salário: '))
print(f'O seu salário é de {salario} e 10% dele é {salario * 0.10} e juntando os dois, é {salario + salario * 0.10}')
