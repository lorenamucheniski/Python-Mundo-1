for random import shuffle
n1= str (input('Primeiro aluno(a): '))
n2= str (input('Segundo aluno(a): '))
n3= str (input('Terceiro aluno: '))
n4= str (input('Quarto aluno: '))
lista = [n1,n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)