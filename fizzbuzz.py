fir = int(input())
sec = int(input())
col = int(input())

res = []
for i in range(1, col+1):
    
    if ((i % fir == 0) and (i % sec == 0)):
        res.append ('FB')
    elif (i % fir == 0):
        res.append ('F')   
    elif (i % sec == 0):
        res.append ('B')
    else:
        res.append (str(i))


print(' '.join(res))
