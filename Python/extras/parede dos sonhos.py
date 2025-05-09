M = int(input("Tamanho da área: "))
if M % 5 != 0:
    rolos = int(M / 5) + 1
else:
    rolos = int(M/5)

print (rolos)
