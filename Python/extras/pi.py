pi = 4/1 - 4/3 + 4/5 - 4/7

def pi (n):
    soma = 0
    ímpar = 1
    for k in range(n):
        if k %2 == 0:
            soma = soma + 4 / ímpar
        else:
            soma = soma - 4 / ímpar
        ímpar = ímpar + 2
    return soma
