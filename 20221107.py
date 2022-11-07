#11279

import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if(x == 0):
        if(len(heap) == 0):
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    elif(x > 0):
        heapq.heappush(heap, (-x, x))



#1927

import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if(x == 0):
        if(len(heap) == 0):
            print(0)
        else:
            print(heapq.heappop(heap))
    elif(x > 0):
     heapq.heappush(heap, x)


#11286

import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if(x != 0):
        heapq.heappush(heap, (abs(x), x))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)