n = 0
for x in range (18644, 33088):
        if '2' in str(x) and '7' not in str(x):
            n = n + 1
print (len([x for x in range (18644, 33088) if '2' in str(x) and '7' not in str(x)]))
