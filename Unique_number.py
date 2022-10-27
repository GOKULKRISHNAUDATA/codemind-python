n=int(input())
n=list(str(n))
f=n.copy()
f=set(f)
f=list(f)
if len(n)==len(f):
    print("Unique Number")
else:
    print("Not Unique Number")