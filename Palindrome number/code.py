n = input()
c = 0
for i in range(len(n)):
    if n[i] == n[len(n)-i-1]:
        c = 1
    else:
        c = 0
if c == 1:
    print("Pallindrome")
else:
    print("Not Pallindrome")
    
