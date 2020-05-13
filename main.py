from cores import colors, fundoVermelho, fundoVerde, fundoBranco
from cardapioMontar import cardapio_ou_montar

## Início do MENU:

## Print saudacao de acordo com o hora do dia
## Adiconar precos de entrega
##

linhaVerde= fundoVerde(15*' ')
linhaBranca= fundoBranco(15*' ')
linhaVermelha= fundoVermelho(15*' ')

print(linhaVerde, linhaBranca, linhaVermelha, sep='')
print(colors.white, '{:^45}'.format("Benvindo@ à Pizzaria Don'Ana!"))
print(linhaVerde, linhaBranca, linhaVermelha, sep='')

print('\n','Qual seu nome?')
nome= input(" >> ").capitalize()
print('Olá,', nome, "!")

##Escolher Pizza do cardápio ou montar:
cardapio_ou_montar()























