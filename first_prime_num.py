i=2
a=int(input())
c=[]
while len(c)<a:
    if i==2 or i==3 or i==5 or i==7:
        c.append(i)
    elif i%2!=0 and  i%3!=0 and i%5!=0 and i%7!=0:
        c.append(i)
    i=i+1
print(c)

