M = int(input("Metros a serem pintados: "))
if M % 54 == 0:
    latas = M / 54
else:
    latas = int(M / 54) + 1

valor = latas * 80
print (f' {latas} latas')
print (f'Total: R$ {valor:.2f} ' )
