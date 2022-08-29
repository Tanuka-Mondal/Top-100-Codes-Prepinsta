n = input()
s = str(int(n) * int(n))
if s[len(n):] == n:
    print("Automorphic Number")
else:
    print("Not an automorphic number")
