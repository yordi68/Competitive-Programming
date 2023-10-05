tt = int(input())

while tt:
    number = input()
    five = set(["2","7"])
    zero = set(["0","5"])
    f_cnt = 0
    z_cnt = 0
    
    i = len(number) - 1
    while i >= 0 and number[i] != "5":
        i -= 1
        f_cnt += 1
    j = i - 1
    while j >= 0 and number[j] not in five:
        f_cnt += 1
        j -= 1
        
    k = len(number) - 1
    while k >= 0 and number[k] != "0":
        k -= 1
        z_cnt += 1
        
    l = k - 1
    while l >= 0 and number[l] not in zero:
        z_cnt += 1
        l -= 1

    print(min(z_cnt, f_cnt))
    


    tt -= 1