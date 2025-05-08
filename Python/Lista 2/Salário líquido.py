a.+ Salário Bruto : R$
b.- IR (11%): R$
c.- INSS (8%): R$
d.- Sindicato (5%): R$
e.= Salário Liquido: R$

H = float(input("Ganha por hora: "))
T = float(input("Total de horas trabalhadas no mês: "))
Salário = H * T
IR = Salário * 0.11
INSS = Salário * 0.08
Sindicato = Salário * 0.05
Mensal = Salário - IR - INSS - Sindicato
print (f'Salário R$ {Salário:.2f}')
print (f'-IR: R$ {IR:.2F}')
print (f'-INSS R$ {INSS:.2f}')
print (f'-Sindicato R$ {Sindicato:.2f}')
print (f' = Mensal R$ {Mensal:.2f}')
