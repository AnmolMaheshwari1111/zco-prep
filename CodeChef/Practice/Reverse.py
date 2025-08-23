def reve(a):
    b=a.split(sep=",")    
    c="".join(b).split(sep=".")    
    d="".join(c).split(sep=";")    
    e="".join(d).split(sep="'")    
    f="".join(e).split(sep=":")  
    g="".join(f).split()
    g.reverse()
    return " ".join(g)
l=[]
for i in range(int(input())):
    l.append(reve(input()))
l.reverse()
for j in l:
    print(j)