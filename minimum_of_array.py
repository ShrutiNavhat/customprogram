A=list(map(int, input().split()))
i=0
min_num=A[0]
while i<len(A):
    if A[i]<=min_num:
        min_num=A[i]
    i=i+1
print(min_num)
