n = 0
lista = []
for x in range (0, 10000):
    if '42' in str(x):
        n = n + 1
print (len([x for x in range(0,10000) if '42' in str(x)]))

06 - 06 - def apaga(s,n). Seja uma string s e um inteiro positivo n, retorna uma nova string sem a posição n. Exemplos: apaga('kitten',1) -> 'ktten'.

def apaga(s, n):
  return s[ :n] + s[n+1:]
