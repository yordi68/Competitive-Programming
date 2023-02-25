def solve():
    len_str1, len_str2, k = map(int, input().split())
 
    str1 = list(input())
    str2 = list(input())
    
    str1.sort()
    str2.sort()
    
    output = []
    str1_cnt = 0
    str2_cnt = 0
    i = 0
    j = 0
    
    while i < len_str1 and j < len_str2:
        
        if ((str1[i] < str2[j] and str1_cnt < k) or str2_cnt == k):
            output.append(str1[i])
            str1_cnt += 1
            str2_cnt = 0
            i += 1
            
        else:
            output.append(str2[j])
            str2_cnt += 1
            str1_cnt = 0
            j += 1
    
    print(''.join(output))
    
def main():
    num_tests = int(input())
    
    for i in range(num_tests):
        solve()
 
main()