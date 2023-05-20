n = input()
m = input()
arr = sorted(n)
for i in range(len(arr)):
    if arr[0] == '0' and arr[i] != '0':
        arr[0], arr[i] = arr[i], arr[0]
        break
# print(arr)
if m == "".join(arr):
    print("OK")
else:
    print("WRONG_ANSWER")