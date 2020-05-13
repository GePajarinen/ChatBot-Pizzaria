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
