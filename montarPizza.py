from funcoesMontandoPizza import tamanho_pizza, recheio_borda, rechearPizza, somandoAPizzaMontada

def montar_pizza():

    ##Escolha o tamanho da pizza:
    precoDaMassa = tamanho_pizza()

    ##Tipo de borda:
    precoDaBorda = recheio_borda()

    ## Recheios:
    precoDosRecheios = rechearPizza()

    ##Somar:
    somandoAPizzaMontada(precoDaMassa, precoDaBorda, precoDosRecheios)