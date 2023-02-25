def main():
    num_stacks, height_of_exhibit = map(int, input().split())
    heights = list(map(int, input().split()))
    
    height_to_build = 1
    max_height = max(heights)
    
    heights.sort()
    ans = 0
    
    for i in range(num_stacks):
        #we leave one block in each column and remove the rest
        ans += (heights[i] - 1)
        
        #if the current height is built move to the next
        if heights[i] >= height_to_build:
            height_to_build += 1
            
    
    #subtract number of unbuilt heights from answer
    ans -= (max_height - height_to_build + 1)
    print(ans)

main()