#10989

import sys
input = sys.stdin.readline

n = int(input())
numlist = [0]*10000

for i in range(n):
    a = int(input())
    numlist[a-1] += 1 #계수정렬

for i in range(10000):
    if numlist[i] > 0:
        for j in range(numlist[i]):
            print(i+1)




#1920

import sys
input = sys.stdin.readline

n = int(input())
nlist = set(map(int, input().split()))

m = int(input())
mlist = list(map(int, input().split()))

for i in mlist:
    if i in nlist:
        print(1)
    else:
        print(0)




#10172

print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\__|")



#2738

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlist =[[0 for i in range(m)] for j in range(n)]
mlist =[[0 for i in range(m)] for j in range(n)]

for i in range(n):
    nlist[i] = list(map(int, input().split()))

for i in range(n):
    mlist[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        nlist[i][j] += mlist[i][j]
        print(nlist[i][j], end=' ')
    print()
