# #2164

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
que = deque([i for i in range(1, n+1)])

while(len(que) > 1):
    que.popleft()
    num = que.popleft()
    que.append(num)

print(que[0])



# #15828

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
que = deque([])

num = int(input())
while(num != -1):
    if(num == 0):
        que.popleft()
    elif(num > 0):
        if(len(que) < n):
            que.append(num)
        else:
            que.popleft()
            que.append(num)
    
    num = int(input())
    
if(len(que) == 0):
    print('empty')
else:
    for i in range(len(que)):
        print(int(que[i]), end = ' ')
        
        

#11866

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
que = deque([])

for i in range(1, n+1):
    que.append(i)
    
print('<', end='')

while que:
    for i in range(k-1):
        que.append(que[0])
        que.popleft()
        
    print(que.popleft(), end='')

    if que:
        print(',', end=' ')

print('>')