A=list(map(int, input().split()))
num=int(input())
i=0
c=0
while i<len(A):
    if A[i]==num:
        c=c+1
    i=i+1
if c>=1:
    print("yes")
else:
    print("no")
    
    

