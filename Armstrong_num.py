A=input()
i=0
c=0
while i<len(A):
    c+=int(A[i])**len(A)
    i=i+1
if c==int(A):
    print("yes")
else:
    print("no")

