"""Escrever um algoritmo que lê o nome de um aluno,
as 3 notas obtidas por ele em provas. Para cada aluno, 
calcular a média de aproveitamento, usando a fórmula:    
MA = (Nl + N2 + N3)/3
A atribuição de conceitos obedece à tabela a seguir:
Média de Aproveitamento Conceito >= 9.0 A >= 7.5 e < 9.0 B >= 6.0 e < 7.5 C >= 4.0 e < 6.0 D < 4.0 E 
O algoritmo deve escrever nome do aluno, suas notas, a média de aproveitamento, 
o conceito correspondente e a mensagem: "APROVADO" se o conceito for A, B, ou C e "REPROVADO" se conceito for D ou E.""
ALGORITMO ALUNO       VAR             NOME: CARACTER             MA, N1, N2, N3: REAL      
INÍCIO      ESCREVER (‘ INFORME O NOME DO ALUNO: ’ )  LER ( NOME )  ESCREVER (‘ INFORME AS 3 NOTAS DE ’, NOME)  
LER ( N1, N2, N3 )      MA  ( N1+N2+N3 ) / 3  ESCREVER (‘O ALUNO ’,NOME,‘ OBTEVE AS NOTAS: ’,N1,‘ ’,N2,‘ E ’,N3)  
ESCREVER (‘E SUA MÉDIA É: ’, MA)  SE (MA >= 9) ENTÃO   ESCREVER (‘ OBTENDO O CONCEITO A E ESTÁ APROVADO!’) 
FIM-SE
SE (MA >= 7.5) E (MA < 9.0) ENTÃO   ESCREVER (‘ OBTENDO O CONCEITO B E ESTÁ APROVADO!’)  
FIM-SE SE (MA >= 6) E (MA < 7.5) ENTÃO   ESCREVER (‘ OBTENDO O CONCEITO C E ESTÁ APROVADO!’) 
FIM-SE 
 """
nome=str(input("Digite o nome do aluno: "))
print("Nome do aluno informado: ",nome)
notaum=float(input("Digite a nota 01 do aluno: "))
notadois=float(input("Digite a nota 02 do aluno: "))
notatres=float(input("Digite a nota 03 do aluno: "))
print("As notas do aluno",nome,"foram:",notaum,notadois,notatres)
MA=notaum+notadois+notatres/3
print("Sua média é: ",MA)
if (MA>=9):
    print("O aluno",nome,"obteve conceito A e está aprovado")
elif (MA>=7.5) and (MA<9.0):
    print("O aluno",nome,"OBTEVE CONCEITO B E ESTÁ APROVADO")
elif (MA>=6) and (ma<7.5):
    print("O aluno",nome,"obteve conceito C e está aprovado")
else:
    print("O aluno",nome,"obteve D ou E e está reprovado")
 