n = int(input())
if n == 1:
    print(0)
elif n == 2:
    print([0,1])
else:
    l = [0,1]
    while n>2:
        l.append((l[-1]+l[-2]))
        n-=1
    print(l)        
