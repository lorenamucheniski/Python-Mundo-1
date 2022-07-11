print('========== DESCONTO ==========')
preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 10 / 100)
print('O valor do seu produto de R${:.2f} com o desconto de 10% é igual a R${:.2f}'.format(preco, novo))