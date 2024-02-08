A=list(map(int, input().split()))
B=int(input())
i=0
c=[]
b=0
while i<len(A):
    j=0
    while j<len(A):
        if A[i]+A[j]==B:
            print(A[i],A[j])
        j=j+1
    i=i+1

