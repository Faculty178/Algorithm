# #11660

import sys
input = sys.stdin.readline

#put data
n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
sum_data = [[0] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_data[i][j] = sum_data[i][j-1] + sum_data[i-1][j] - sum_data[i-1][j-1] + data[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    print(sum_data[x2][y2] - sum_data[x1-1][y2] - sum_data[x2][y1-1] + sum_data[x1-1][y1-1])
    
    
# #10986

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
sums = [0]*n
sums[0] = nums[0]
ans = 0

for i in range(1, n):
    sums[i] = sums[i-1] + nums[i] 

lefts = [0]*m

for i in range(n):
    rem = sums[i] % m
    if (rem == 0):
        ans += 1
    
    lefts[rem] += 1

for i in range(m):
    if lefts[i] > 1:
        ans += (lefts[i]*(lefts[i]-1)//2)



print(ans)



#7568

import sys
input = sys.stdin.readline

n = int(input())
people = []

for _ in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height))

rank = []

for i in range(n):
    cnt = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    rank.append(cnt)

for i in rank:
    print(i, end=' ')