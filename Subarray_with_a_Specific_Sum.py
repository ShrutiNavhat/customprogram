A=list(map(int, input().split()))
B=int(input())
i=0
c=0
d=[]
while i<len(A):
    if c<B:
        c=c+A[i]
        d.append(A[i])  
    elif c>B:
        c=0
        d=[]
    else:
        c=c
        d=d
        break
    i=i+1
print(d)
