S=input()
i=0
c=0
c1=0
c2=0
while i<len(S):
    if len(S)>=8:
        if S[i]=="!" or S[i]=="@" or  S[i]=="#" or S[i]=="$" or S[i]=="%" or S[i]=="&" or S[i]=="*" or S[i]=="?" or S[i]=="/" or S[i]=="|":
            c=c+1
        elif S[i]=="1" or S[i]=="0"or S[i]=="1" or S[i]=="2" or S[i]=="3" or S[i]=="4" or S[i]=="5" or S[i]=="6" or S[i]=="7" or S[i]=="8" or S[i]=="9":
            c1=c1+1
        else:
            c2=c2+1
    i=i+1
if c>=1 and c1>=1 and c2>=1:
    print("yes")
else:
    print("no")

