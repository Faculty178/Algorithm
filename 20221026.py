#1764

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = set()
mlist = set()

for _ in range(n):
    nlist.add(input())

for _ in range(m):
    mlist.add(input())

ans = sorted(list(nlist & mlist))

print(len(ans))
print(''.join(ans), end='')





#2609

import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
print(math.gcd(n, m))
print(math.lcm(n, m))




#1934

import math
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    n, m = map(int, input().split())
    print(math.lcm(n, m))