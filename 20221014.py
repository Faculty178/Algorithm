#1436

n = int(input())
ans = 0
devil = 666

while True:
    if '666' in str(devil):
        ans = ans + 1
    if ans == n:
        print(devil)
        break
    devil = devil + 1




#1193

n = int(input())
line = 1

while n>line:
    n -= line
    line += 1

if line%2 == 0:
    m = n
    s = line - n + 1
else :
    m = line - n + 1
    s = n

print(m, '/', s, sep='')




#2581

m = int(input())
n = int(input())
ans = []

for i in range(m, n+1):
    for j in range(2, i+1):
        if j == i:
            ans.append(i)
        if i % j == 0:
            break


if (len(ans)==0):
    print(-1)
else:
    print(sum(ans))
    print(min(ans))



