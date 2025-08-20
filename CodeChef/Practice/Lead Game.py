n=int(input())
lead=0
leader=0
p1=0
p2=0
for _ in range(n):
    a,b =map(int,input().split())
    p1+=a
    p2+=b
    if p1>p2 and (p1-p2)>lead:
        lead = (p1-p2)
        leader = 1 
    if p2>p1 and (p2-p1)>lead:
        lead = (p2-p1)
        leader = 2 
print(leader , lead)