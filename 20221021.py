#25305

n, k = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort(reverse = True)

print(scores[k-1])


#2108

from collections import Counter

numbers = []
n = int(input())

for _ in range(n):
	numbers.append(int(input()))

#avg	
print(round(sum(numbers)/n))

#mean
numbers.sort()
print(numbers[int((n-1)/2)])

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

