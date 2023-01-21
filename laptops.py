n = int(input())
 
a = []
 
for i in range(n):
    a.append(tuple(int(x) for x in input().split()))
a.sort(key=lambda x:x[0])
x = "Poor Alex"
_max = 0
for i in range(len(a) - 1):
    if a[i][1] > a[i + 1][1]:
        x = "Happy Alex"
print(x)
