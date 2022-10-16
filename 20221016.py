#11654

a = input()
print(ord(a))


#3009

lista = []
listb = []
x = 0
y = 0

for _ in range(3):
    a, b = map(int, input().split())
    lista.append(a)
    listb.append(b)

for i in range(3):
    if lista.count(lista[i]) == 1:
        x = lista[i]
    
    if listb.count(listb[i]) == 1:
        y = listb[i]

print(x, y)

