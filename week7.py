# 7주차 DFS/BFS

# 최대공약수 계산 (유클리드 호제법)
"""
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b , a % b)

# 두 자연수 A, B에 대해서 (A>B) A를 B로 나눈 나머지를 R이라고 한다.
# 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
"""

# 음료수 얼려 먹기
"""
def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
        
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True # 사실상 하나라도 0이 되게 되면 True를 return
    return False # 하나라도 0이 아니면 False를 return
    
n,m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input()))
    
result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True: # 해당 좌표가 0이면 무조건 True를 반환 , 해당 노드는 연결가능한 모든 점을 1로 바꿈
            result = result+1
            
print(result)
"""

# 미로탈출
"""
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
        return graph[n-1][m-1]

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

print(bfs(0,0))
"""
