def cut_rod_memoized(price, n, memo):
    if n <= 0:
        return 0
    if memo[n] >= 0:
        return memo[n]
    
    max_val = -float('inf')
    for i in range(n):
        max_val = max(max_val, price[i] + cut_rod_memoized(price, n - i - 1, memo))
    
    memo[n] = max_val
    return max_val

def cut_rod(price, n):
    memo = [-1] * (n + 1)
    return cut_rod_memoized(price, n, memo)

if __name__ == "__main__":
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(arr)
    print(cut_rod(arr, size))
