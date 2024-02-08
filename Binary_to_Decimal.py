A=input()
i=1
b=1
c=0
d=[]
while c<len(A):
    b=i
    i=i+b
    c=c+1
    d.append(b)
j=0
c1=0
while j<len(d):
    if A[(len(A)-1)-j]=="1":
        c1=c1+d[j]
    j=j+1
print(c1)
