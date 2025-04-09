## Solution for 'connectedCell'
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
import math

def connectedCell(matrix):
   # Write your code here

   M, N = len(matrix), len(matrix[0])

   def dfs(i, j):
      if i < 0 or i >= M:
         return 0
      if j < 0 or j >= N:
         return 0
      if matrix[i][j] == 0:
         return 0
      ans = 1
      matrix[i][j] = 0
      for di in range(-1, 2):
         for dj in range(-1, 2):
            ans += dfs(i + di, j + dj)
      return ans
     
   ans = 0
   for i in range(M):
      for j in range(N):
         ans = max(ans, dfs(i, j))
   return ans

def main():

   n = int(input().strip())

   m = int(input().strip())

   matrix = []

   for _ in range(n):
      matrix.append(list(map(int, input().rstrip().split())))

   result = connectedCell(matrix)
   print(result)