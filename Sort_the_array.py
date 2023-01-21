n = int(input())
a = list(map(int,input().split()))
l = 0
r = 0
b = (sorted(a)).copy()
for i in range(n - 1):
    temp = []
    l = i
    r = i
    flag  = 0
    while r < n - 1 and a[r] > a[r + 1]:
        flag = 1
        temp.append(a[r])
        r += 1
    if flag:
        temp.append(a[r])
        temp.reverse()
        a[l:r + 1] = temp
        break
if a == b:
    print("yes")
    print(l + 1,end=" ")
    print(r + 1)
    # break
else:
    print("no")
    # break
