#2108

from collections import Counter
import sys

numbers = []
n = int(sys.stdin.readline())

for _ in range(n):
	numbers.append(int(sys.stdin.readline()))

#avg	
print(round(sum(numbers)/n))

#mean
numbers.sort()
print(numbers[int(n/2)])

#cnt
cnt = Counter(numbers).most_common()
if(len(cnt)) > 1:
	if cnt[0][1] == cnt [1][1]:
		print(cnt[1][0])
	else:
		print(cnt[0][0])
else:
	print(cnt[0][0])
	

#range
print(numbers[-1] - numbers[0])



