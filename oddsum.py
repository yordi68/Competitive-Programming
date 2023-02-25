def main():
    half = int(input())
    
    nums = list(map(int, input().split()))
    nums.sort()
    
    if nums[0] == nums[-1]:
        print(-1)
    else:
        print(*nums)

main()