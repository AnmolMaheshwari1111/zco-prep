# cook your dish here
import math

def longest_dividing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    best = {}  # value -> best length

    for i in range(n):
        val = arr[i]
        max_len = 1

        # find all divisors of val
        limit = int(math.isqrt(val))
        for d in range(1, limit + 1):
            if val % d == 0:
                if d in best:
                    max_len = max(max_len, best[d] + 1)
                other = val // d
                if other in best:
                    max_len = max(max_len, best[other] + 1)

        dp[i] = max_len
        if val in best:
            best[val] = max(best[val], dp[i])
        else:
            best[val] = dp[i]

    return max(dp)


# Input reading
N = int(input().strip())
arr = [int(input().strip()) for _ in range(N)]
print(longest_dividing_subsequence(arr))
