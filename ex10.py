print('========== REAJUSTE SALARIAL ==========' )
salario = float(input('Qual é o salário do funcionário?'))
novo = salario + (salario * 15 / 100)
print('Com o aumento de 15% na folha de pagamento, o novo salário do funcionário será de {:.2f}'.format(novo))