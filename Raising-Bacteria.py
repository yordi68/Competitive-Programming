x = int(input())
count = 0
while x:
    if x % 2 != 0:
        count += 1
    x //= 2
print(count)