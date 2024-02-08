A=list(map(int, input().split()))
i=0
product=1
while i<len(A):
    product=product*A[i]
    i=i+1
print(product)
