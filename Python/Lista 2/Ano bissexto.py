Ano = int(input("O ano é: "))
if  Ano % 4 == 0 and (Ano % 100 != 0 or Ano % 400 == 0):
    print ("Bissexto")
else:
 print ("Não é Bissexto")
