def dma(s):
    if '-' in s:
        return print(s.split('-'))
    elif '/' in s:
        return print(s.split('/'))
    else:
        return print(s)
        


dma('08-11-2024')
dma('08/11/2024') 
dma('08 do 11 de 2024')
