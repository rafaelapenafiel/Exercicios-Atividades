from random import sample
números  = sample (range (100), 20)
pares = []
ímpares = []
for x in números:
    if x%2 == 0:
        pares.append (x)
    if x%2 != 0:
        ímpares.append (x)
        
print ('Números: ', números)
print (f'Par: {pares}')
print (f'Ímpar: {ímpares}')
