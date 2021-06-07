# 11주차 최단경로

# 다익스트라 알고리즘★★★★★★★★ (그리디) O(n^2)
"""
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 10억정도의 수

n,m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
visited = [False] * (n+1) # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
distance = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    a,b,c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append(b,c)

def get_smallest_node():
    min_value = INF
    index=0
    for i in range(1, n+1):
        if (distance[i] < min_value) and (not visited[i]):
            min_value = distance[i]
            index = i
        return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] # 해당 위치까지 가는데 현재는 그정도의 비용이 든다.

    for i in range(n-1):
        now = get_smallest_node() # 노드의 개수보다 적은 수만큼
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print(" 무야호 ")
    else:
        print(distance[i])
"""

# 힙 Heap ( 삽입시간 O(logN) , 삭제시간 O(logN) ) https://littlefoxdiary.tistory.com/3
"""
#최소 힙
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
        
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
    
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#최대 힙
import heapq

def heapsort(iterable):
    h = []
    result = []
    
    for value in interable:
        heapq.heappush(h, -value) # 마이너스
        
    for i in range(len(h)):
        result.append(-heapq.heappop(h)) # 마이너스
    result result
    
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

# 힙을 사용한 다익스트라 ( O(ElogV) E는 간선의 개수)
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1))
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q) # 거리와 현재 노드 번호
        if distance[now] < dist: # 기본 distance는 무한대로 설정 
            continue
        for i in graph[now]: # 현재위치의 node 번호들을 따꺼내서
            cost = dist + i[1] # 현재 노드까지의 거리와 이동가능한 노드들의 거리를 더해서
            if cost < distance[i[0]]: # 만약 이동하려는 노드들의 비용이 더 적다면
                distance[i[0]] = cost # 바꿔주고
                heapq.heappush(q,(cost,i[0])) # 해당 노드를 heapq에 push
                
dijkstra(start)
"""

# 플로이드 워셜 알고리즘★★★★★★★★ (다이나믹 프로그래밍) ( O(N^3) )
"""
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a,b,c = map(int ,input().split())
    graph[a][b] = c
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b])
            
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY",end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
"""

# 전보
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q= []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0])))

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))
    
dijkstra(start)

count = 0

max_distance = 0
for d in distance:
    if d != 1e9:
        count = count+1
        max_distance = max(max_distance, d)
        
print(count-1 , max_distance)
"""

# 미래 도사 ( 플로이드 워셜 알고리즘 )
"""
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n + 1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[a][b] = 1
    
x, k = map(int ,input().split())

for k in range(1, n+1):
    for a in range(1, n+1):   
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)
"""
