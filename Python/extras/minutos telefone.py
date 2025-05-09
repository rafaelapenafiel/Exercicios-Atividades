Minutos = int(input("Minutos falados: "))
if Minutos < 200:
   preço = 0.20
else:
  if Minutos <= 400:
     preço = 0.18
  else:
    preço = 0.15
print (f'R$ {preço*Minutos:.2f}')
