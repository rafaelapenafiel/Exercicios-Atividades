def gato_miando (miando, hora):
    if miando:
        if hora > 22 or hora < 5:
            return True
        else:
            return False
    else:
        return False

print (gato_miando(True, 3))       #True
print (gato_miando(True, 12))     #False
print (gato_miando(False, 2))      #False
