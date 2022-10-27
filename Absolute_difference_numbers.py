N,X=map(int,input().split())
P=str(N)
A=""
B=""
for i in range(X):
    A=A+P[i]
for i in range(-X,0):
    B=B+P[i]
print(abs(int(A)-int(B)))
    