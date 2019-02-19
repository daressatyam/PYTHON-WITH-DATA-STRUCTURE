def addpoly(p1, p2):
    r = []  # Empty list to store the result
    for i in range(len(p1)):
        # Perform addition for elements which match their exponents
        for j in range(len(p2)):
            if p1[i][1] == p2[j][1]:
                r += [(p1[i][0] + p2[j][0], p1[i][1])]

        # Add elements of p1 to r, whose exponents didn't match
        for k in range(len(r)):
            if r[k][1] == p1[i][1]:
                break
        else:
            r += [p1[i]]

    # Add elements of p2 to r, whose exponents didn't match
    for j in range(len(p2)):
        for k in range(len(r)):
            if r[k][1] == p2[j][1]:
                break
        else:
            r += [p2[j]]

    r = [(c, e) for (c, e) in r if c != 0]  # Removes 0 coefficient tuples
    r.sort(key= lambda l : l[1], reverse=True) # Sorts w.r.t. exponents

    return r


def multpoly(p1, p2):
    r = []  # Empty list to store the result

    # Perfom multiplication and result, polynomial addition to previous result
    for i in range(len(p1)):
        for j in range(len(p2)):
            r = addpoly([(p1[i][0] * p2[j][0], p1[i][1] + p2[j][1])], r)

    return r