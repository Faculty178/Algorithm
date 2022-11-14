#2908

a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])

if (a > b):
    print(a)
else:
    print(b)
    

#2630

import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
ans = []

def solution(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != paper[i][j] :
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 0 :
        ans.append(0)
    else :
        ans.append(1)
        
solution(0, 0, N)
print(ans.count(0))
print(ans.count(1))