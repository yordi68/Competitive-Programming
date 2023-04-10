n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int , input().split())))
from collections import defaultdict
adjList = defaultdict(list)
source = set()
sink = set()

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 1:
            source.add(row + 1)
            sink.add(col + 1)
src = []
sync = []
for number in range(1, n + 1):
    if number not in sink:
        src.append(number)
    if number not in source:
        sync.append(number)


print(len(src) , *(src))
print(len(sync) , *(sync))