A=input()
S=input()
i=0
c=0
while i<len(A):
    j=0
    while j<len(S):
        if A[i]==S[j]:
            if A[i+1]==S[j+1]:
                c=c+1
            else:
                c=0
    i=i+1
if c>=1:
    print("yes")
else:
    print("no")
