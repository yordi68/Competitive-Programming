n = int(input())
arr = list(map(int,input().split()))
pre = [0]
post = [0]
new = list(reversed(arr))
for i in range(1,len(arr) + 1):
    pre.append(pre[i - 1] + arr[i - 1])
    post.append(post[i - 1] + new[i - 1])   
post.pop(0)
pre.pop(0)
ed = 0
a = 0
l = 0
r = 0
while l < len(pre) and r < len(post):
    if l + r == len(pre):
        break
    if pre[l] <= post[r]:
        ed += 1
        l += 1
    else:
        a += 1
        r += 1

print(ed,a)