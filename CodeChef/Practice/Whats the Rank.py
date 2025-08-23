def update(bit, i, delta, n):
    while i <= n:
        bit[i] += delta
        i += i & -i

def query(bit, i):
    s = 0
    while i:
        s += bit[i]
        i -= i & -i
    return s

N = int(input().strip())
wealth = [int(input().strip()) for _ in range(N)]

# Coordinate compression
sorted_wealth = sorted(wealth)
comp = {v: i + 1 for i, v in enumerate(sorted_wealth)}
n_comp = len(sorted_wealth)
bit = [0] * (n_comp + 1)

for w in wealth:
    pos = comp[w]
    greater = query(bit, n_comp) - query(bit, pos)
    rank = greater + 1
    print(rank)
    update(bit, pos, 1, n_comp)