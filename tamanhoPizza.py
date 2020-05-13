from tabulate import tabulate

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
