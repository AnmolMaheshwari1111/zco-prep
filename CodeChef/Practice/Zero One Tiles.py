N = int(input())
MOD = 15746

if N == 0:
    print(1)
elif N == 1:
    print(1)
else:
    prev2 = 1  # f(0)
    prev1 = 1  # f(1)
    for _ in range(2, N + 1):
        current = (prev1 + prev2) % MOD
        prev2 = prev1
        prev1 = current
    print(current)