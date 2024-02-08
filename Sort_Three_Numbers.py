A,B,C=map(int, input().split())
b=[0]*3
if A>=B and A>=C:
    b[2]=A
elif B>=A and B>=C:
    b[2]=B
else:
    b[2]=C
if A<=B and A<=C:
    b[0]=A
    if B<=C:
        b[1]=B
    elif C<=B:
        b[1]=C
    elif C>=A and C>=B:
        b[2]=C
    else:
        b[2]=B
elif B<=A and B<=C:
    b[0]=B
    if A<=C:
        b[1]=A
    elif C<=A:
        b[1]=C
    elif C>=A and C>=B:
        b[2]=C
    else:
        b[2]=A
else:
    b[0]=C
    if A<=B:
        b[1]=A
    elif B<=A:
        b[1]=B
    elif A>=B and A>=C:
        b[2]=C
    else:
        b[2]=B
print(b)
