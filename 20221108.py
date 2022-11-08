#2566

import sys
input = sys.stdin.readline

board = []

for _ in range(9) :
    board.append(list(map(int, input().split())))
    
pointX = 0
pointY = 0
ans= -999

for i in range(9):
    for j in range(9):
        if board[i][j] > ans:
            ans = board[i][j]
            pointX = i+1
            pointY = j+1

print(ans)
print(pointX, pointY)


#2447

def draw_stars(n):
    if n==1:
        return ['*']

    Stars=draw_stars(n//3)
    L=[]

    for star in Stars:
        L.append(star*3)
    for star in Stars:
        L.append(star+' '*(n//3)+star)
    for star in Stars:
        L.append(star*3)

    return L

N=int(input())
print('\n'.join(draw_stars(N)))