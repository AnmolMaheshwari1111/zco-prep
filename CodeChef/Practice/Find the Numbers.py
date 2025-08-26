def backtrack(idx, k, remainingSum, remainingProduct, current):
    if idx == k:
        return remainingSum == 0 and remainingProduct == 1, current
    for val in range(1, remainingSum+1):
        if remainingProduct % val != 0:
            continue
        current.append(val)
        found, sol = backtrack(idx+1, k, remainingSum - val, remainingProduct // val, current)
        if found:
            return True, sol
        current.pop()
    return False, None

S, P, k = map(int, input().split())
found, sol = backtrack(0, k, S, P, [])
if found:
    print(" ".join(map(str, sol)))
else:
    print("NO")