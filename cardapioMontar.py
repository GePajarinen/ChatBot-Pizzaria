from cores import colors
from funcoesDoCardapio import ver_cardapio
from montarPizza import montar_pizza

def cardapio_ou_montar():

    print("Escolha uma opção:", '\n',
         colors.yellow, "1", colors.reset, "para conhecer o nosso", colors.underline,"cardápio", colors.reset,'\n',
         colors.yellow, "2", colors.reset,"para", colors.underline ,"montar", colors.reset, "a sua pizza")
    escolha = int(input(">> "))

    if escolha == 1:
        return ver_cardapio()
    elif escolha == 2:
        return montar_pizza()
    else:
        print(colors.red,">>Escolha inválida. Tente novamente.<<", colors.reset)
        return cardapio_ou_montar()