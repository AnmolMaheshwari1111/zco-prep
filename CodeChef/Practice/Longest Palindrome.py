a=int(input())
b=input()
length=0
word=''
for i in range(0,len(b)):
    for j in range(i+1,len(b)+1):
        if b[i]==b[j]:
            if b[i:j]==b[i:j][::-1]:
                if len(b[i:j])>length:
                    length=len(b[i:j])
                    word=b[i:j]
print(length)
print(word)