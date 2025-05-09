Minutos = int(input("Minutos falados: "))
if Minutos < 200:
   preço = 0.20
elif Minutos <= 400:
  preço = 0.18
elif Minutos <=800:
  preço = 0.15
else:
     preço = 0.08
print (f'R$ {preço*Minutos:.2f}')
