A=int(input())
i=1
c=0
while i<A:
    if A%i==0:
        c=c+i
    i=i+1
if c==A:
    print("yes")
else:
    print("no")

