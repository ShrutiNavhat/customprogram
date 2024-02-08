n=int(input())
i=1
while i<=10:
   if n%2==0:
     if n%i!=0:
       print("not prime")
       break
   else:
     print("prime")
     break
   i=i+1
