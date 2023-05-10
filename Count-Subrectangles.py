def count_ones(segments, cnt):
    i = 0
    n = len(segments)

    while i < n:
        j = i
        while j < n and segments[j] == 1:
            j += 1

        len_ones = (j - i)
        count = 1
        while len_ones > 0:
            cnt[len_ones] += count
            len_ones -= 1
            count += 1

        i = j + 1


n, m, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_cnt = [0] * (n + 1)
b_cnt = [0] * (m + 1)

count_ones(a, a_cnt)
count_ones(b, b_cnt)

cnt = 0
for i in range(1, n + 1):
    idx = k // i
    mod = k % i

    if idx <= m and mod == 0:
        cnt += (a_cnt[i] * b_cnt[idx])

print(cnt)