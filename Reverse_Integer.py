N=int(input())
P=""
S=""
A=str(N)
if(A[0]=='-'):
    P=A[0]
    A=A[1:]
for i in A:
    S=i+ S
L=int(S)
print(P+str(L))