a, b = map(int, input().split())
v = [b]

while b > 0:
    if b % 2 == 0:
        b //= 2
        v.append(b)
    elif (b - 1) % 10 == 0:
        b -= 1
        b //= 10
        v.append(b)
    else:
        break
    if b == a:
        break



if v[-1] != a:
    print("NO")
else:
    print("YES")
    n = len(v)
    print(n)
    for i in range(n-1, -1, -1):
        print(v[i], end=' ')
