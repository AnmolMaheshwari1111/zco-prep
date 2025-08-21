# Need to fix Urgently
c = []
def mss(x, h, l):
    m = (h+l)//2
    if c[m+1] >x and c[m]>x:
        h = m
        mss(x, h, l)
    elif c[m]<x and c[m+1]<x:
        l = m
        mss(x, h, l)
    else:
        c.insert(m+1, x)
n, m = map(int, input().split())
for _ in range(n+m):
    i = int(input())
    if i == -1:
        print(c.pop())
    else:
        if len(c) == 0:
            c.append(i)
        elif c[-1] == c[0]:
            if c[0]>i:
                c.insert(0, i)
            else:
                c.append(i)
        elif c[-1] < i:
            c.append(i)
        elif c[0]>i:
            c.insert(0, i)
        else:
            mss(i, len(c)-1, 0)