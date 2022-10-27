N=int(input())
p=0
for i in range(1,N//2):
    if(i*(i+1)==N):
        p=1
        break
if (p==1):
    print("YES")
else:
    print("NO")