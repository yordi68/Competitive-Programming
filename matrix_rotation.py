def solve():
    ROWS, COLS = 2, 2
    matrix = []
    
    for i in range(ROWS):
        matrix.append(list(map(int,input().split())))
    
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    
    for i in range(ROWS):
        for j in range(COLS):
            if matrix[i][j] < matrix[x1][y1]:
                x1, y1 = i, j
            
            if matrix[i][j] > matrix[x2][y2]:
                x2, y2 = i, j
    
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    if dx + dy > 1:
        print("YES")
    else:
        print("NO")

def main():
    num_tests = int(input())
    
    for test in range(num_tests):
        solve()

main()