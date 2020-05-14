from tabulate import tabulate
from cores import colors

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
    m = len(opcoesDeRecheio)

    for i in range(n):
        x = int(listadeingredientes[i])

        precosIgre = opcoesDeRecheio[x - 1][2]
        precoDaCadaIngrediente = float(precosIgre[1:5])

        if x <= m:
            print('-', opcoesDeRecheio[x - 1][1])
            precosDosIngrediente.append(precoDaCadaIngrediente)

        # else: # Refazer
        #     print("O código {} não está na lista de ingredientes.".format(listadeingredientes[i]), '\n',
        #           "Digite 'ok' para recomeçar: ")
        #
        #     tab = input(">> ").lower()
        #
        #     while tab != 'ok':
        #         print("Digite 'ok' para recomeçar: ")
        #
        #         tab = input(">> ").lower()
        #
        #         return rechearPizza()



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