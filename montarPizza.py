from tamanhoPizza import tamanho_pizza
from recheioBordas import recheio_borda
from recheandoPizza import rechearPizza
from somandoPizzaMontada import somandoAPizzaMontada

def montar_pizza():

    ##Escolha o tamanho da pizza:
    precoDaMassa = tamanho_pizza()

    ##Tipo de borda:
    precoDaBorda = recheio_borda()

    ## Recheios:
    precoDosRecheios = rechearPizza()

    ##Somar:
    somandoAPizzaMontada(precoDaMassa, precoDaBorda, precoDosRecheios)
