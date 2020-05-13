from cores import colors

def somandoDoCardapio(indexDaPizza, lista, tamanhoDaPizza):
    total = lista[indexDaPizza][tamanhoDaPizza]
    print('O Total do seu pedido é de:', colors.yellow, total)
