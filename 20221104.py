#4153

import sys
input = sys.stdin.readline

while(1):
    nums = list(map(int, input().split()))
    nums.sort()

    if(nums[0] == 0 and nums[1]== 0 and nums[2]==0):
        break 

    if(nums[0]*nums[0] + nums[1]*nums[1] == nums[2]*nums[2]):
        print('right')
    else:
        print('wrong')


