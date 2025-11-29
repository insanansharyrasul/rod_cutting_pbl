def cut_rod(price, n):
    if n <= 0:
        return 0
    max_val = -float('inf')
    for i in range(n):
        max_val = max(max_val, price[i] + cut_rod(price, n - i - 1))
    return max_val

if __name__ == "__main__":
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(arr)
    print(cut_rod(arr, size))
