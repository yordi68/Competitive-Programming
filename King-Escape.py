n = int(input())
a1, a2 =  list(map(int, input().split()))
b1, b2 = list(map(int, input().split()))
t1, t2 = list(map(int, input().split()))


flag = 0

if (b1 < a1 and t1 < a1) or (b1 > a1 and t1 > a1):
    if (b2 < a2 and t2 < a2) or (b2 > a2 and t2 > a2):
        flag = 1

if flag:
    print("YES")
else:
    print("NO")
