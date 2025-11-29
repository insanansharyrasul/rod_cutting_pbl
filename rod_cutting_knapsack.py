def cut_rod_knapsack(price, n):
    dp = [0 for _ in range(n + 1)]

    for i in range(len(price)):
        length = i + 1
        val = price[i]
        for w in range(length, n + 1):
            dp[w] = max(dp[w], val + dp[w - length])
            
    return dp[n]

if __name__ == "__main__":
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(arr)
    print(cut_rod_knapsack(arr, size))
