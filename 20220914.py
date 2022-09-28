#11720
n = input()
numbers=list(input())
sum = 0

for i in numbers:
    sum = sum + int(i)

print(sum)


# #1546
n = int(input())
tlist = list(map(int, input().split()))
tmax = max(tlist)
sum = sum(tlist)

print(sum*100/tmax/n)


#11659
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum=[0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(m):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])

    
#11660


