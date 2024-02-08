A=list(map(int, input().split()))
i=0
c=0
while i<len(A):
    if A[i]<0:
        c=c+1
    i=i+1
if c>=1:
    print("yes")
else:
    print("no")
