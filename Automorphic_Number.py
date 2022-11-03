a=int(input())
b=a**2
c=str(a)
d=b%10**len(c)
if d==a:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")