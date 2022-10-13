def getSum(n):
    sum=0
    for digit in str(n):
        sum+=int(digit)
    return sum
    
n=int(input())
x=n*n
e=getSum(x)
if(e==n):
    print("Neon Number")
else:
    print("Not Neon Number")