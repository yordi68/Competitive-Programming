n = int(input())
for i in range(n):
     r,m = list(map(int,input().split()))
     mat = []
     for i in range(r):
          mat.append(list(map(int,input().split())))
     from collections import defaultdict
     row = len(mat)
     col = len(mat[0])
     diagonal = defaultdict(int)
     anti_diagonal = defaultdict(int)
     for i in range(row):
          for j in range(col):
               diagonal[i + j] += mat[i][j]
               anti_diagonal[j - i] += mat[i][j]
 
     _max = 0
     for i in range(row):
          for j in range(col):
               if diagonal[i + j] + anti_diagonal[j - i] - mat[i][j] > _max:
                    _max = diagonal[i + j] + anti_diagonal[j - i] - mat[i][j]
 
     print(_max)
