
from tabulate import tabulate
from cores import colors


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