""" Faça um algoritmo que leia a altura e o sexo de uma pessoa,
calcule seu peso ideal, utilizando as seguintes fórmulas:
#para homens : (72.7*altura) –58; 
#para mulheres : (62.1*altura) – 44.7.

"""

sexo=str(input("Informe o sexo da pessoa M/F: "))
print("Sexo informado: ", sexo)
altura=float(input("Informe a sua altura: "))
if sexo =='f':
    pi=62.1*altura-44.7
    print("Seu peso ideal será de: ",pi)
    
elif sexo =='m':
    pi=72.7*altura-58
    print("Seu peso ideal será de:",pi)