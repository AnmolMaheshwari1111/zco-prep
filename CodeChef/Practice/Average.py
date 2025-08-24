n=int(input())
l=[int(input().strip()) for _ in range(n)]
e=[]
o=[]
for i in l:
    if i%2:
        e.append(i)
    else:
        o.append(i)
def dif(l:list)->list:
    for i in range(0,len(l)-2):
            