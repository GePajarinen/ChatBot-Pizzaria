from cores import colors

def somandoAPizzaMontada(valorMassa, tipoDeBorda, totalDosRecheios):
    total = float(valorMassa + tipoDeBorda + totalDosRecheios)
    print('O total a pagar é de:',colors.yellow, total, 'R$', colors.reset)
