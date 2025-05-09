def inverte (frase):
    palavras = frase.split()
    palavras_invertidas = palavras[ : : -1]
    return print  (' '.join(palavras_invertidas))

inverte('batatinha quando nasce')
