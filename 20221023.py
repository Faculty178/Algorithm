#3003

chess = [1, 1, 2, 2, 2, 8]
a = list(map(int, input().split()))

for i in range(len(chess)):
    print(chess[i] - a[i], end=' ')
    
#1152

word = input().split()
print(len(word))