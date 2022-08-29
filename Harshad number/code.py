n = int(input())
sum = 0
flag = n
while flag > 0:
    sum += flag%10
    flag = flag//10
if n % sum == 0:
    print("Harshad Number")
else:
    print("Not a harshad number")
    
