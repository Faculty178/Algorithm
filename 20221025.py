#10814

import sys
input = sys.stdin.readline

n = int(input())
member = []

for _ in range(n):
    member.append(list(input().split()))

member.sort(key = lambda x : int(x[0]))

for i in range(n):
    print(member[i][0], member[i][1])
    




#2587

import sys
input = sys.stdin.readline

nums = [0]*5
for i in range(0, 5):
    nums[i] = int(input())

nums.sort()
ans1 = sum(nums)

print(int(ans1/5))
print(nums[2])





#18870

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

indexes = sorted(list(set(nums)))
dic = {indexes[i]: i for i in range(len(indexes))}

for i in nums:
    print(dic[i], end = ' ')



