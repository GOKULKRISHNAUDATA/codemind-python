n=int(input())
sum=0
temp=n
while n:
    i=1
    fact=1
    r=n%10
    while i<=r:
        fact*=i
        i+=1
    sum+=fact
    n=n//10
if(sum==temp):
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")
        