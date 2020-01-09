def player_stat_dict(file):
    """
    Opens the file holding the box score stats collected and creates a giant list
    with smaller lists for each player
    [name, points, offensive RB, defensive RB, Assists, Steals, Blocks, Turnover,
    free throws made off of passes, field goals, field goals attempted,
    free throws, free throws attempted, personal fouls]
    """
    large_lst = []
    final_dict = {}
    f = open(file, 'r')
    for i in f.readlines():
        stats = i.split(', ')
        large_lst.append(stats)
    for i in large_lst:
        i[-1] = i[-1][:-1]
        final_dict[i[0]] = i[1:]
    print(final_dict)
    return large_lst

def game_score(P, ORB, DRB, A, S, B, TO, A2FTM, FG, FGA, FT, FTA, PF):
    """
    creates a game score value given a player's box stats. Based off of John
    Hollinger's equation but slightly modified to fit my own philosophies and
    the college game.
    In order:
    points, offensive RB, defensive RB, Assists, Steals, Blocks, Turnover,
    free throws made off of passes, field goals, field goals attempted,
    free throws, free throws attempted, personal fouls
    """
    sc = (P + 0.7*A + 0.2*A2FTM + 0.7*ORB + 0.3*DRB + S + B - TO -
    0.3*(FGA - FG) - 0.2*FTA - FT - 0.3*PF)
    return sc

def game_score_per_player(l):
    """
    prints each player's game score on the team.
    """
    for i in l:
        scr = game_score(int(i[1]), int(i[2]), int(i[3]), int(i[4]), int(i[5]),
        int(i[6]), int(i[7]), int(i[8]), int(i[9]), int(i[10]), int(i[11]),
        int(i[12]), int(i[13]))
        str = '{}: {}'.format(i[0], round(scr, 2))
        print(str)
