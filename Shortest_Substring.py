n = int(input())
 
for k in range(n):
    _min = float("inf")
    st = input()
    ptr1 = -1
    ptr2 = -1
    ptr3 = -1
    for i in range(len(st)):
        if ptr1 != -1 and ptr2 != -1 and ptr3 != -1:
            left = min(ptr1,ptr2,ptr3)
            right = max(ptr1,ptr2,ptr3)
            _min = min(_min,right - left + 1)
        if st[i] == str(1):
            ptr1 = i
        elif st[i] == str(2):
            ptr2 = i
        elif st[i] == str(3):
            ptr3 = i
        # print()
    if ptr1 != -1 and ptr2 != -1 and ptr3 != -1:
        left = min(ptr1,ptr2,ptr3)
        right = max(ptr1,ptr2,ptr3)
        _min = min(_min,right - left + 1)
    print(_min if _min != float("inf") else 0)
