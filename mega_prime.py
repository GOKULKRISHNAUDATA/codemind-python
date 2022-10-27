N=int(input())
p=0
if (N==1 or N==0):
    p=1
for i in range(2,int(N*(0.5))+1):
    if (N%i==0):
        p=1
        break
M=str(N)
for i in M:
    A=int(i)
    if (A==1 or A==0):
        p=1
    for j in range(2,int(A*(0.5))+1):
        if(A%j==0):
            p=1
            break
if(p==0):
    print("Mega Prime")
else:
    print("Not Mega Prime")