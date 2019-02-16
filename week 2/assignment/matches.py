def matched(s):
    ss = []
    balanced = True
    index = 0
    while index < len(s) and balanced:
        token = s[index]
        if token == "(":
            ss.append(token)
        elif token == ")":
            if len(ss) == 0:
                balanced = False
            else:
                ss.pop()

        index += 1

    return balanced and len(ss) == 0