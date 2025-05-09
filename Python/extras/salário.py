joao = 10000
josé = 5000
anos = 0
while joao > josé:
    if anos < 3:
        joao = joao + joao*0.03
        josé = josé + josé*0.1
        anos = anos + 1
    elif anos == 3:
        joao = joao + joao*0.1
        josé = josé + josé*0.1
print (anos)
