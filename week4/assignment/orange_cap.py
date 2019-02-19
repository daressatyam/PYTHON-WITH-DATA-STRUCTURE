def orangecap(d):
    score = {}
    for match in d:
        for player in d[match]:
            if player in score:
                score[player] += d[match][player]
            else:
                score[player] = d[match][player]

    (playername, topscore) = ("", 0)
    for player in score:
        if score[player] > topscore:
            topscore = score[player]
            playername = player
    return (playername, topscore)



