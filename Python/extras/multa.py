V = int(input("Velocidade do carro: "))
multa = (V - 110) * 5
if V > 110:
    print ("Você foi multado")
    print (f'Multa R$ {multa:.2f}')
if V < 110:
    print ("Você se livrou")
