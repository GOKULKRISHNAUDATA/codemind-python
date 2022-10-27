Hurl,Spin,Speed=map(int,input().split())
if(Hurl > 50 and Spin > 60 and Speed > 100):
    print(10)
elif(Hurl > 50 and Spin > 60):
    print(9)
elif(Spin > 60 and Speed > 100):    
    print(8)
elif(Hurl > 50 and Speed > 100):
    print(7)
elif(Hurl > 50 or Spin > 60 or Speed > 100):
    print(6)
else:
    print(5)