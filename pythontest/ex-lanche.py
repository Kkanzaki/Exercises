pedido=input('Digite a opçao desejada \n1 para Big Super Sanduba \n2 para Quase Super Sanduba \n3 para Mirradus Sanduba\n')

big=['opção1','R$5,00']
qs=['opção2','R$3,00']
ms=['opção3','R$1,50']

if pedido == '1':
    print('Você pediu a',big[0],'que custa R$',big[1])
elif pedido == '2':
    print('Você pediu a',qs[0],'que custa R$',qs[1])
else:
    print('Você pediu a',ms[0],'que custa R$',ms[1])
    