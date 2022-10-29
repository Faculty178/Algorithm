#10807

import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
num = int(input())

print(nums.count(num))


#5597

import sys
input = sys.stdin.readline
bad = [i for i in range(1, 31)]

for _ in range(28):
	bad.remove(int(input()))

print(min(bad))
print(max(bad))



# #2292
import sys
input = sys.stdin.readline
n = int(input())
bee = 1
cnt = 1

while n > bee:
	bee += 6 * cnt
	cnt += 1
	
print(cnt)
	  

