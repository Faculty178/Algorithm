#14888

import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))
op = list(map(int, input().split()))

min_num = int(1e9)
max_num = -int(1e9)

def dfs(depth, total, plus, minus, multiply, divide):
    global max_num, min_num
    if depth == n:
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(max_num)
print(min_num)



#4949

import sys
input = sys.stdin.readline

while True :
    a = input().rstrip()
    stack = []

    if a == "." :
        break

    true_flag = 1
    for cha in a:
        if cha == '(' or cha == '[':
            stack.append(cha)
        elif cha == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                true_flag = 0
                break
        elif cha == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                true_flag = 0
                break

        
    print("yes" if true_flag and not(stack) else "no")

