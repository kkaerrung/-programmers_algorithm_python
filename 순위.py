def solution(n, results): 
    win, lose ={}, {}
    for i in range(1, n+1): 
        win[i], lose[i] = set(), set()

    for i in range(1, n+1): 
        for battle in results:
            if battle[0] == i: 
                win[i].add(battle[i])
            if battle[i] == i: 
                lose[i].add(battle[0])
        for winner in lose[i]: 
            win[winner].update(win[i])

        for loser in win[i]: 
            lose[loser].update(lose[i])

    count = 0
    for i in range(1, n+1): 
        if len(win[i]) + len(lose[i]) == n -1:
            count += 1
    return count