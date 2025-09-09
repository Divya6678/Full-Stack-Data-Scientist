def prime(n):
    f=False
    for i in range(2,n):
        if n%i==0:
           return False
    else:
        return True
a=prime(23)
if a:
    print("Prime")
else:
    print("Not Prime")