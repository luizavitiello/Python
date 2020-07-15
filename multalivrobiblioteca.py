"Calcular a multa que deve ser paga por um estudante que atrasou a entrega de um livro na biblioteca"


dias_com_livro=int(input("Informe quantos dias o aluno permaneceu com o livro: "))
print("O aluno ficou",dias_com_livro,"dias com o livro")
multa_a_ser_paga=float(input("Informe o valor da multa que o aluno deve pagar: "))
total=dias_com_livro*multa_a_ser_paga
print("O total em R$ que o aluno irá pagar será de: R$",total)