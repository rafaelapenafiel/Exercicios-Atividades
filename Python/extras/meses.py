meses = '''janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'''.split ()
d, m, a = input('dd/mm/aaaa').split ('/')
m = int (m)
print (f' {d} de {meses[m - 1]} de {a}')

