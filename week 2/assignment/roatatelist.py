def rotatelist(l, k):
    if not l:
        return l
    return [l[i % len(l)] for i in range(k, k + len(l))]