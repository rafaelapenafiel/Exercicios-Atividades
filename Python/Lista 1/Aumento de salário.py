salário = float(input('Salário: '))
porcentagem = int(input('Aumento%: '))
aumento = salário * porcentagem / 100
novo = salário + aumento
print (f'Aumento: R$ {aumento:.2f}')
print (f'Novo salário: R$ {novo:.2f}')
