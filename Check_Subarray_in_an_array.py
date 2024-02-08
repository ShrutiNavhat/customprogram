a=list(map(int, input().split()))
b=list(map(int, input().split()))
i=0
c=0
while i<len(a):
    j=0
    while j<len(b):
        if a[i]!=b[j]:
            c=c+1
            break
        j=j+1
    i=i+1
if c<1:
    print("yes")
else:
    print("no")

