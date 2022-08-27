s = input()
sum = 0
for i in range(len(s)):
    sum += int(s[i]) ** len(s)
if sum == int(s):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
