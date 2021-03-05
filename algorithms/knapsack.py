def knapsack(w, ws, vs):
    if (not ws):
        return -1
    
    ws = [0] + ws 
    vs = [0] + vs 
    n_ws = len(ws)
    n_w = w + 1
    dp = [[0] * n_w for _ in range(n_ws)]

    max_weight = 0
    for y in range(1, n_ws):
        for x in range(1, n_w):
            if (x - ws[y] >= 0):
                dp[y][x] = max(dp[y - 1][x - ws[y]] + vs[y],
                               dp[y - 1][x])
            else:
                dp[y][x] = dp[y - 1][x]
            
            max_weight = max(max_weight, dp[y][x])

    return max_weight