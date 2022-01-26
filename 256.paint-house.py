def minCost(costs):
    m = len(costs)
    dp = [[float('inf') for _ in range(3)] for _ in range(m)]

    dp[0] = costs[0]

    for i in range(1, m):
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
    
    return min(dp[m-1])
