#1269

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a-b) + len(b-a))


#1655
import sys
import heapq
input = sys.stdin.readline

leftHeap=[]
rightHeap=[]
ans=[]

N=int(sys.stdin.readline())

for i in range(N):
    inputNum=int(sys.stdin.readline())

    if len(leftHeap)==len(rightHeap):
        heapq.heappush(leftHeap, (-inputNum, inputNum))
    else:
        heapq.heappush(rightHeap, (inputNum, inputNum))

    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        min=heapq.heappop(rightHeap)[0]
        max=heapq.heappop(leftHeap)[1]
        heapq.heappush(leftHeap, (-min, min))
        heapq.heappush(rightHeap, (max, max))

    ans.append(leftHeap[0][1])
    
for j in ans:
    print(j)