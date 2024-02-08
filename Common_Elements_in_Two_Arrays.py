    
a=list(map(int, input().split()))
b=list(map(int, input().split()))
i=0
c=[]
c1=0
while i<len(a):
    j=0
    while j<len(b):
        if a[i]==b[j]:
            c.append(a[i])
            break
        j=j+1
    i=i+1
print(c)
