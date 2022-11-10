#2981

import sys
input = sys.stdin.readline

N = int(input())
nums = sorted([int(input()) for _ in range(N)])
minus = []

for i in range(1, N):
    minus.append(nums[i] - nums[i-1])
    
def findGCD(a, b):
    num = b
    div = a
    rest = num % div
    while rest != 0:
        num = div
        div = rest
        rest = num % div
    return div

GCD = minus[0]
for idx in range(1, len(minus)):
    GCD = findGCD(GCD, minus[idx])

result = set()
for i in range(2, int(GCD**0.5) + 1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD // i)
result.add(GCD)
print(*sorted(list(result)))



#11050

from math import factorial
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

ans = factorial(n) // (factorial(m)*factorial(n-m))
print(ans)
