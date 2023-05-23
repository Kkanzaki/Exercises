n1 = input('Primeiro nome:')
p1 = float(input('Peso: '))
n2 = input('Segundo nome:')
p2 = float(input('Peso:'))

class People():
    def __init__(self,nome,peso):
        self.nome = nome
        self.peso = peso
    def __str__(self):
        return f"{self.nome}({self.peso})"
        
p1 = People(n1,p1)
p2 = People(n2,p2)

if p1.peso>p2.peso :
    print('O',p1.nome,'é o mais pesado com',p1.peso,'Kg')
else:
    print('O é o mais pesado e',p2.nome,'é o mais pesado com',p2.peso,'Kg')
