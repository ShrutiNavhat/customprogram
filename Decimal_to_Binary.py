a=int(input())
i=a
b=0
c=[]
while i>=1:
    b=(i%2)
    i=i//2
    c.append(b)
j=0
while j<len(c):
    print(c[(len(c)-1)-j],end="")
    j=j+1

