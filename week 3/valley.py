def valley(l):
 if (len(l) < 3):
    return False
 ucount = 1
 lcount = 1
 for i in range(0, len(l) - 1):
    if l[i] > l[i + 1]:
        if lcount > 1:
            return False
        ucount = ucount + 1
    if l[i] < l[i + 1]:
        lcount = lcount + 1
    if l[i] == l[i + 1]:
        return False
 if ucount >1 and lcount > 1:
    return True
 else:
    return False