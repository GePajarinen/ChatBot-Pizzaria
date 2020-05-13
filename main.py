from tabulate import tabulate

class colors:
    reset = '\033[0m'
    underline = '\033[04m'
    white = '\033[30m'
    green = '\033[32m'
    yellow = '\033[93m'
    red = '\033[31m'

def fundoVermelho(skk):
    return "\033[41m {}\033[m" .format(skk)
def fundoBranco(skk):
    return "\033[40m {}\033[m".format(skk)
def fundoVerde(skk):
    return "\033[42m {}\033[m".format(skk)


def tamanho_pizza():
    opceosDeTamanhos = [(1,'Pequena (20cm)','+1.00R$'),
                        (2,'Média (25cm)','+1.25R$'),
                        (3,'Grande (35cm)','+1.50R$'),
                        (4,'Família (50cm)','+2.50R$')
    ]

    cabecalhoDosTamanhos = ['Código', 'Tamanho', 'Preço à adicionar']

    print("Nós temos 4 tamanhos de pizza:", '\n')
    print(tabulate(opceosDeTamanhos, headers=cabecalhoDosTamanhos))

    print("Digite o código do tamanho da pizza que gostaria:", '\n')

    tam = int(input(">> "))
    tamanho = opceosDeTamanhos[tam-1][2]
    precoDaMassa = float(tamanho[1:5])

    return precoDaMassa

def recheio_borda():
    print("Gostaria de bordas recheadas?", '\n',
          colors.yellow,"1",colors.reset,"- Não, obrigado.", '\n',
          colors.yellow,"2",colors.reset,"- Sim, com mussarela (+0.50R$)", '\n',
          colors.yellow,"3",colors.reset,"- Sim, com Cheddar (+0.70R$)")

    borda: int = int(input(">> "))

    if borda >= 4:
        print(fundoVermelho(">>Escolha inválida. Tente novamente.<<"))
        return recheio_borda()
    else:
        if borda == 1:
             precoDaBorda = 0
        elif borda == 2:
            precoDaBorda = 0.50
        else:
             precoDaBorda = 0.70

    return precoDaBorda


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

def ver_cardapio():

    listadepizzas = [(1,'Americana', "Presunto, champignon e requeijão salpicado com bacon crocante", '2,5R$', '5,00R$', '7,5R$', '12,5R$'),
          (2,'Atum', 'Atum sólido com finas fatias de cebola cobertura de muçarela ou requeijão', '5,5R$', '10,00R$', '17,5R$', '22,5R$'),
          (3,'Baiana', 'Calabresa moída, ovos, pimenta, cebola e leve toque de parmesão', '3,5R$', '6,00R$', '8,5R$', '13,5R$'),
          (4,'Abobrinha', 'Abobrinha, bacon crocante e leve cobertura de muçarela ou requeijão', '2,5R$', '5,00R$', '7,5R$', '12,5R$'),
          (5,'Frango com Catupiry', 'Frango desfiado e milho cobertos com Catupiry', '2,5R$', '5,00R$', '7,5R$', '12,5R$'),
          (6,'Calabresa', 'Calabresa fatiada e finas fatias de cebola', '3,5R$', '6,00R$', '8,5R$', '13,5R$'),
          (7,'Quatro Queijos', 'Muçarela, provolone, gorgonzola e parmesão', '5,5R$', '8,00R$', '10,5R$', '17,5R$'),
          (8,'Lombinho', 'Lombinho e cebola cobertos com muçarela ou requeijão', '6,5R$', '9,00R$', '11,5R$', '20,5R$'),
          (9,'Italiana', 'Muçarela, rodelas de tomate, parmesão e folhas de manjericão', '2,5R$', '5,00R$', '7,5R$', '12,5R$'),
          (10,'Vegetariana', 'Palmito, brócolis, milho, champignon e leve cobertura de muçarela', '4,5R$', '7,00R$', '9,5R$', '14,5R$')
          ]
    cabecalho= ['Código','Pizza', 'Ingredientes', 'Pequena (20cm)', 'Média (25cm)', 'Grande (35cm)', 'Família (50cm)']

    print(tabulate(listadepizzas, headers=cabecalho), '\n')

    print('Qual o código da pizza que gostaria de pedir?')
    codigoDaPizza= input('>> ')
    indexDaPizza= int(codigoDaPizza)-1

    print("Pizza de {}".format(listadepizzas[indexDaPizza][1]), 'de qual tamanho?')

    print(colors.yellow, "1",colors.reset,"- Pequena", '\n',#index 3
          colors.yellow, "2",colors.reset,"- Média", '\n',# index 4
          colors.yellow, "3",colors.reset,"- Grande", '\n', # index 5
          colors.yellow, "4",colors.reset,"- Família") #index 6

    escolhaDoTamanho= input('>> ')
    indexDoTamanho = int(escolhaDoTamanho)+2

    somandoDoCardapio(indexDaPizza, listadepizzas, indexDoTamanho)

def somandoDoCardapio(indexDaPizza, lista, tamanhoDaPizza):
    total = lista[indexDaPizza][tamanhoDaPizza]
    print('O Total do seu pedido é de:', colors.yellow, total)

def rechearPizza():
    print('Escolha os ingredientes para montar a sua pizza:', '\n')
    opcoesDeRecheio = [
        (1,'queijo mussarela','+2.00R$'),
        (2,'presunto','+2.90R$'),
        (3,'tomate','+2.00R$'),
        (4,'cebola','+0.50R$'),
        (5,'azeitona','+1.00R$'),
        (6,'molho de tomate','+0.50R$'),
        (7,'cogumelos','+2.00R$'),
        (8,'frango','+1.50R$'),
        (9,'lombo','+2.00R$'),
        (10,'costela de porco','+2.00R$'),
        (11,'salame','+1.50R$'),
        (12,'pimentão','+0.50R$'),
        (13,'abobrinha','+0.90R$'),
        (14,'cheddar','+2.00R$'),
        (15,'chocolate ao leite','+2.00R$'),
        (16,'chocolate meio amargo','+2.00R$'),
        (17,'chocolate branco','+2.00R$'),
        (18,'morangos','+2.50R$'),
        (19,'uvas','+2.00R$'),
        (20,'pêssegos', '+2.00R$')]

    cabecalhorecheios = ('Código','Recheio', 'Preço adicional')

    print(tabulate(opcoesDeRecheio, headers=cabecalhorecheios))

    print('Digite o código o recheio separados por "Espaço"', '\n')

    listadeingredientes = list(input('>> ').split())
    print("Você adicionou na sua pizza:", '\n')

    n = len(listadeingredientes)
    precosDosIngrediente = []

    for i in range(n):
        x = int(listadeingredientes[i])
        precosIgre = opcoesDeRecheio[x - 1][2]
        precoDaCadaIngrediente = float(precosIgre[1:5])

        try:
            print('-', opcoesDeRecheio[x - 1][1])
            precosDosIngrediente.append(precoDaCadaIngrediente)

        except IndexError as error:
            print("O código {} não está na lista de ingredientes.".format(listadeingredientes[i]), '\n',
                  "Digite 'ok' para recomeçar: ")

            tab = input(">> ").lower()

            while tab != 'ok':
                print("Digite 'ok' para recomeçar: ")
                tab = input(">> ").lower()

            return rechearPizza()




    print("Se estiver tudo certo, digite",colors.yellow,"'Ok'", colors.reset)
    print("Se quiser mudar alguma coisa, digite",colors.yellow,"'9'", colors.reset)

    decisao = input('>> ').lower()

    while decisao != 'ok' and decisao !='9':
        print("Digite 'Ok' se estiver tudo certo ou '9' para refazer a pizza")
        decisao = input('>> ').lower()

    if decisao == 'ok':
        somaPrecosIngredientes = sum(precosDosIngrediente)
        return somaPrecosIngredientes

    elif decisao == '9':
        return rechearPizza()


def somandoAPizzaMontada(valorMassa, tipoDeBorda, totalDosRecheios):
    total = float(valorMassa + tipoDeBorda + totalDosRecheios)
    print('O total a pagar é de:',colors.yellow, total, 'R$', colors.reset)


def montar_pizza():

    ##Escolha o tamanho da pizza:
    precoDaMassa = tamanho_pizza()

    ##Tipo de borda:
    precoDaBorda = recheio_borda()

    ## Recheios:
    precoDosRecheios = rechearPizza()

    ##Somar:
    somandoAPizzaMontada(precoDaMassa, precoDaBorda, precoDosRecheios)


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























