# 5주차 완전탐색

# 상하좌우
"""
n = int(input()) # 5
x,y = 1,1
plans = input().split() # R R R U D D

dx = [0,0,1,-1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny

print(x,y)
"""

# 최고의 13위치
"""
n=5
gird = {
[0,0,0,0,0],
[0,1,0,0,0],
[0,0,1,0,1],
[0,0,0,0,0],
[0,0,0,1,0]
}

def GetNumOfGold(row,col_s,col_e):
    num_of_gold=0
    
    for col in range(col_s,col_e+1):
        num_of_gold = num_of_gold + grid[row][col]
    return num_of_gold
    
max_gold=0

for row in range(0,n):
    for col in range(0,n):
        if col + 2 >=: continue
        
        num_of_gold = GetNumOfGold(row,col,col+2)
        max_gold = max(max_gold, num_of_gold)
        
print(max_gold)
"""

# 시각
"""
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count = count+1
                
print(count)
"""

# 왕실의 나이트
"""
input_data = input()
row = int(input[1])
column = int(ord(input_data[0]))-int(ord('a')) + 1 # ord 는 해당 문자의 유니코드 값을 돌려주는 함수

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result=0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result = result+1
        
print(result)
"""

# 문자열 재정렬
"""
data=input()
result=[]
value=0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
        
result.sort()

if value != 0:
    result.append(str(value))
    
print(''.join(result))
"""
