n = int(input())
for i in range(n):
    st = input()
    st_set = set()
    j = 0
    while j < len(st):
        if (j + 1) == len(st) or st[j] != st[j + 1]:
            st_set.add(st[j])
            j += 1
        else:
            j += 2
    print(''.join(sorted(list(st_set))))
