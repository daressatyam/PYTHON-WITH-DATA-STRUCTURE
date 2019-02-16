def matrixflip(m,d):
    tempm = m.copy()
    if d=='h':
        for i in range(0,len(tempm),1):
                tempm[i].reverse()
    elif d=='v':
        tempm.reverse()
    return(tempm)