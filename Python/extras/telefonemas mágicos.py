def resposta(f):
    if '42' in f:
        return True
    else:
        return False

print(resposta('421234'))       #True
print(resposta('123442'))       #True
print(resposta('124245'))       #True
print(resposta('123456'))       #False
