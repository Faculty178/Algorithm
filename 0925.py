#11004
A, B = map(int, input().split())
Mlist = list(map(int, input().split()))
Mlist.sort()
print(Mlist[B-1])

#2751
n = int(input())
newlist = [0]*n
for i in range(len(newlist)):
    newlist[i] = int(input())
    
newlist.sort()
for i in range(len(newlist)):
    print(newlist[i])