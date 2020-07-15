"""Faça um algoritmo que leia um número inteiro e indique se ele é divisível por 2. ALGORITMO DIVISIVEL_2 
VAR 
 X: INTEIRO 
INÍCIO 
 ESCREVER (‘ INFORME UM NÚMERO INTEIRO: ’); 
 LER (X) 
 SE ( X MOD 2 = 0 ) ENTÃO 
  ESCREVER ( X, ‘ É DIVISÍVEL POR 2 ’) 
SENÃO 
  ESCREVER ( X, ‘ NÃO É DIVISÍVEL POR 2 """
  
n=int(input("Informe um número inteiro: "))
print("Número digitado: ",n)
if n%2==0:
    print(n,"é divisível por 2")
else:
    print(n,"Não é divisível por 2")