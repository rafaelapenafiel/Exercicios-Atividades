cigarros = int(input('Cigarros por dia: '))
anos = int(input('Anos fumando: '))
total_cigarros = anos * 365 * cigarros
dias = total_cigarros / 144
print (f'Você perdeu {dias:.1f} dias')
