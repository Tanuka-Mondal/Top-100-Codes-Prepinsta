n = int(input())
c = 0
if n>1:
    for i in range(2,n//2 + 1):
        if n%i == 0:
           c+=1
    if c == 0:
        print("Prime")
    else:
        print("Not prime")
else:
    print("Not prime")
