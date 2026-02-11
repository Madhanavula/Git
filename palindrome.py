i=123
n=i
rev=0
while n!=0:
    m=n%10
    rev=rev*10+m
    n=n//10

if rev==i:
    print("its pal")
else:
    print("its not pal")

