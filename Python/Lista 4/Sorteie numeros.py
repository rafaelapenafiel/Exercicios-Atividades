from random import sample
números  = sample (range (100), 10)
maior = 0
menor = 101
for x in números [1: ]:
    if x > maior: maior = x
    if x < menor: menor = x

print ('Números: ', números)
print (f'Maior: {maior}')
print (f'Menor: {menor}')
