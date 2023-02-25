def main():
    ROWS, COLS, k = map(int, input().split())
    
    seats = []
    for i in range(ROWS):
        seats.append(input())
     
    #find number of ways to arrange seats in each row   
    num_ways = 0
    for row in range(ROWS):
        empty_slots = 0
        
        for col in range(COLS):
            if seats[row][col] == '.':
                empty_slots += 1
            else:
                empty_slots = 0
            
            if empty_slots >= k:
                num_ways += 1
    
    #find number of ways to arrange seats in each column
    for col in range(COLS):
        empty_slots = 0
        
        for row in range(ROWS):
            if seats[row][col] == '.':
                empty_slots += 1
            else:
                empty_slots = 0
            
            if empty_slots >= k:
                num_ways += 1
    
    #handle k = 1 case
    if k == 1:
        num_ways //= 2
    
    print(num_ways)
 
main()