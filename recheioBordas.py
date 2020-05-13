from cores import colors

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
