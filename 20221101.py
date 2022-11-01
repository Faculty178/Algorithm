#9012

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    stack = []
    new = input()
    for j in new:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: 
                print("NO")
                break
    else: 
        if not stack: 
            print("YES")
        else: 
            print("NO")
			

#18258

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
que = deque([])

for _ in range (n):
    

#~제출 전 for문은 tab을 한번 할 것
	
	new = input().split()

	if (new[0] == 'push'):
		que.append(new[1])
		
	elif(new[0] == 'pop'):
		if not que:
			print(-1)
		else:
			print(que.popleft())
		
	elif(new[0] == 'size'):
		print(len(que))
		
	elif(new[0] == 'empty'):
		if(len(que) != 0):
			print(0)
		else:
			print(1)
			
	elif(new[0] == 'front'):
		if(not que):
			print(-1)
		else:
			print(que[0])
	
	elif(new[0] == 'back'):
		if (not que):
			print(-1)
		else:
			print(que[-1])