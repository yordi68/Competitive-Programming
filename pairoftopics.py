length = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
diff = [0] * length

for i in range(length):
    diff[i] = arr1[i] - arr2[i]

diff.sort()

total = 0
beg = 0
end = length - 1

# find pairs which gives Di + Dj > 0
while end >= beg:
    while beg < end and diff[beg] + diff[end] <= 0:
        beg += 1

    total += max(end - beg, 0)
    end -= 1

print(total)