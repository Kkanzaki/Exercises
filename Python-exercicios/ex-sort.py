nome=input('Nome do aluno: ')
n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
n3=float(input('Terceira nota: '))

notas=[n1,n2,n3]
media=(n1+n2+n3)/3
if media >= 6:
    print('O aluno',nome,'foi aprovado com',media,'de media')
else:
    print('O aluno',nome,'foi reprovado com',media,'de media')

notas.sort(reverse=True)
print(notas)