menu = int(input('Digite o código do prato desejado para saber mais\n1 - Miojo\n2 - Pão\n3 - Suco\n4 - Lanche\n5 - Sopa\n'))

class Menu():
    def __init__(self,cod,desc):
        self.cod = cod
        self.desc = desc
    def __str__(self):
        return f"{self.cod}({self.desc})"

mj = Menu(1,"Macarrao Instantaneo\nSabor Galinha Caipira\nCom tempero Sazon")
p = Menu(2,'Pão de Forma com:\n1 - Presunto\n2 - Mussarela\n3 - Cenoura\n4 - Alface\n5 - Maionese')
su = Menu(3,'Suco Natural com sabores de:\nAcerola\nAbacaxi com Hortelã\nLaranja\nUva')
la = Menu(4,'X-burguer contendo:\nPão de Hot Dog\nHamburguer\nSalada de Alface\nPicles\nKetchup\nQueijo Prato\nBatata palha\n')
so = Menu(5,"Sopa Nutritiva com:\nPedaços de Carne Bovina\nBatata Doce\nMandioca\nBatata\nMilho")
        
if menu == mj.cod:
    print(mj.desc)
elif menu == p.cod:
    print(p.desc)
elif menu == su.cod:
    print(su.desc)
elif menu == la.cod:
    print(la.desc)
else:
    print(so.desc)
