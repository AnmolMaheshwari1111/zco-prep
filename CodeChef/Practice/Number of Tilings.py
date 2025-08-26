def tile(n:int)->int:
    if n==1: return 1
    if n==2: return 2
    if n==3: return 3
    else:
        return tile(n-1)+tile(n-2)+tile(n-3)
for i in range(1,100):
    print(tile(i))