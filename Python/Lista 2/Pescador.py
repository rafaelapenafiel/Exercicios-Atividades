P = float(input("Peso do peixe:"))
multa = (P - 50) * 4
if P > 50:
    print ("João pagará multa")
    print (f'multa R$ {multa:.2f}')
else:
    print ("João não foi multado")
