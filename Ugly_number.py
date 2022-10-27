def isugly(n):
    while n%2==0:
        n=n//2
    if n==1:
        return True
    while n%3==0:
        n=n//3
    if n==1:
        return True
    return False
n=int(input())
if isugly(n):
    print("Ugly Number")
else:
    print("Not Ugly Number")