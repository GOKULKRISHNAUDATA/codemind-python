A=int(input())
B=int(input())
P=0
Q=0
for i in range(1,A):
    if(A%i==0):
        P=P+i
for i in range(1,B):
    if(B%i==0):
        Q=Q+i
if(P==B and Q==A):
    print("Amicable")
else:
    print("Not Amicable")