def isPrime(n):
    c = 0
    if n>1:
        for i in range(2,n//2 + 1):
            if n%i == 0:
               c+=1
        if c == 0:
            print(n)
        
l,h = map(int,input().split())
for i in range(l,h):
    isPrime(i)
