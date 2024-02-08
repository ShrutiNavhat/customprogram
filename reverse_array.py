A=list(map(int, input().split()))
i=0
reverse_arr=[]
b=0
while i<len(A):
    b=(len(A)-1)-i
    reverse_arr.append(A[b])
    i=i+1
print(reverse_arr)
