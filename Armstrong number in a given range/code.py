def armstrongCheck(s):
    s = str(s)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i]) ** len(s)
    if sum == int(s):
        print(s)
l,h = map(int,input().split())   
for i in range(l,h+1):
    armstrongCheck(i)
