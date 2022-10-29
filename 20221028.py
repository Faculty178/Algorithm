#11650

import sys
input = sys.stdin.readline

n = int(input())
points = []


for _ in range(n):
	[x, y] = map(int, input().split())
	points.append([x, y])
	
points = sorted(points)

for i in range(n):
	print(points[i][0], points[i][1])
	
	



#11651

import sys
input = sys.stdin.readline

n = int(input())
points = []

for _ in range(n):
	[x, y] = map(int, input().split())
	points.append([y, x])

points = sorted(points)


for i in range(n):
	print(points[i][1], points[i][0])
	



