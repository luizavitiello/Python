"""Escrever um algoritmo que lê o número de um vendedor de uma empresa,
seu salário fixo e o total de vendas por ele efetuadas. Cada vendedor recebe um salário fixo,
mais uma comissão proporcional às vendas por ele efetuadas.
A comissão é de 3% sobre o total de vendas até R$ 1.000,00 e 5% sobre o que ultrapassa este valor.
Escrever o número do vendedor, o total de suas vendas, seu salário fixo e seu salário total. 
ALGORITMO SALARIO VAR  NV: CARACTER  TV, SFIXO, SFINAL:
REAL INÍCIO  ESCREVER (‘ INFORME O NÚMERO DE REGISTRO DO VENDEDOR: ’ ) 
LER ( NV )  ESCREVER (‘ INFORME O SALARIO FIXO DO VENDEDOR: ’)  LER ( SFIXO ) 
ESCREVER (‘ INFORME O TOTAL DE VENDAS DO VENDEDOR: ’)  
LER ( TV )  SE ( TV < 1000 ) ENTÃO   SFINAL  SFIXO + (TV * 3) /100 """

n_vendedor=float(input("Digite o número do vendedor: "))
print("Número digitado: ",n_vendedor)
salario_fixo=float(input("Informe o salário do vendedor: "))
total_vendas=int(input("Informe o total de vender realizadas pelo vendedor: "))
if total_vendas<1000:
    sfinal=salario_fixo+(total_vendas*3/100)
    print("O salário final do vendedor será de: ",sfinal) 
elif total_vendas>1000:
    sfinal=salario_fixo+(total_vendas*5/100)
    print("O salário final do vendedor será de: ",sfinal)
