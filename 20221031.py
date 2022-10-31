#2559

import sys
input = sys.stdin.readline

days, num = map(int, input().split())
temps = list(map(int, input().split()))
sums = []

sums = sum(temps[:num])
ans = sums

for i in range(num, days):
	sums += temps[i] - temps[i-num]
	ans = max(ans, sums)
	
print(ans)



# #10828

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):

	line = input().split()

	if(line[0] == 'push'):
		stack.append(line[1])
		
	elif(line[0] == 'top'):
		if(len(stack) != 0):
			print(stack[-1])
		else:
			print(-1)
			
	elif(line[0] == 'size'):
		print(len(stack))

	elif(line[0] == 'empty'):
		if(len(stack) != 0):
			print(0)
		else:
			print(1)

	elif(line[0] == 'pop'):
		if(len(stack) == 0):
			print(-1)
		else:
			print(stack.pop())




# #10773

import sys
input = sys.stdin.readline

k = int(input())
stack = []

for _ in range(k):
	
	num = int(input())
	
	if(num != 0):
		stack.append(num)
	else:
		stack.pop()

print(sum(stack))



	
	
	
	