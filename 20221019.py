#14425

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = set([input() for _ in range(N)])
cnt = 0
for _ in range(M):
    t = input()
    if t in s:
        cnt += 1
print(cnt)



#10816

import sys
input = sys.stdin.readline

N = int(input())
cards = [*map(int, input().split())]
M = int(input())
candidate = [*map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in candidate:
    result = count.get(target)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")