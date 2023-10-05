n = int(input())



inputs = list(map(int,input().split(" ")))
list1 = []
count = 0
# max1 = float("-inf")
# min1 = float("inf")

for i in range(n):
    if list1:
        max1 = max(list1)
        min1 = min(list1)
        if inputs[i] > max1:
            max1 = inputs[i]
            count += 1
        elif inputs[i] < min1:
            min1 = inputs[i]
            count += 1
    list1.append(inputs[i])

print(count)
