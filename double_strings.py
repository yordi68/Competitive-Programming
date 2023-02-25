def solve():
    num_strings = int(input())
    strings = []
    
    for i in range(num_strings):
        string = input()
        strings.append(string)
    
    indices = set(strings)
    ans = ['0' for i in range(num_strings)]
    for i in range(num_strings):
        for j in range(1, len(strings[i])):
            prefix = strings[i][: j]
            suffix = strings[i][j :]
            
            if prefix in indices and suffix in indices:
                ans[i] = '1'
    
    return ''.join(ans)

def main():
    num_tests = int(input())
    
    for test in range(num_tests):
        print(solve())

main()