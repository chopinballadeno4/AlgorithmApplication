# 12 기다 그래프 이론

# 서로소 집합 자료구조
"""
def find_parent(parent, x):
    if parent[x]  != x:
        return find_parent(parent, parent[x])
    return x

def find_parent(parent, x): # 경로 압축 사용용
   if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a , b)

print('각 원소가 속한 집합: ', end ='')
for i in range(1, v+1):
    print(find_parent(parent,i), end=' ')

print()

print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
"""

# 서로소 집합을 활용한 사이클 판별
"""
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_parent(parent, a , b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i
    
cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 발생 ㄴㄴ")
"""

# 크루스칼 알고리즘 ( 간선의 개수가 E개 일때 O(ElogE)
"""
def find_parent(parent, x): # 서로소 집합을 통해 사이클 판별 알고리즘?
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_parent(parent,a ,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e =map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i
    
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost,a ,b))
    
edges.sort() # 튜플 첫번째 원소를 기준으로 정렬? https://penguingoon.tistory.com/207

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a ) != find_parent(parent, b):
        union_parent(parent, a, b)
        result = reuslt + cost
        
print(result)
"""

# 위상 정렬 특징 ( 순환하지 않은 방향 그래프에서만 사용가능 O(E+V) )
"""
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1) # 진입차수
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, inutput().split())
    graph[a].append(b)
    indegree[b] = indegree[b] + 1
    
def topology_sort():
    result = []
    queue = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        now = queue.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] = indegree[i] - 1 # 해당 진입차수를 1씩 빼다가
            if indegree[i] == 0: # 0 이 되는 것을 넣자
                queue.append(i)
                
    for i in result:
        print(i, end=' ')

topology_sort()
"""
