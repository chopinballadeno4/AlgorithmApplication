 # 10주차 DP

# 피보나치 수열 (탑다운, 버텀업)
"""
#탑다운 (메모이제이션 O(N))
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
    
print(fibo(99))
실행결과 -> f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4)

#버텀업
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
    
print(d[n])
"""

# 개미 전사
"""
n = int(intput())
array = list(map(int,input().split()))

d = [0] * 100
d[0] = array[0]
d[1] = max(array[0] , array[1])

for i in range(2, n):
    d[i] = max(d[i-1] , d[i-2] + array[i])
    
print(d[n-1])
"""

# 1로 만들기
"""
x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] +1
    if i & 2 ==0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 ==0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 ==0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])
"""

# 효율적인 화폐 구성
"""
n, m = map(int , input().split())

array= []

for i in range(n):
    array.append(int(input()))
    
d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j] , d[j - array[i]]+1)
            
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
    
# 가방문제랑 유사한듯 ? 
"""

# 금광
"""
for tc in range(int(input())):
    n, m = map(int,input().split())
    array = list(map(int, input().split()))
    dp = []
    index =0
    
    for i in range(n):
        dp.append(array[index:index+m]_
        index = index+m
        
    for j in range(1, m):
        for i in range(n):
            if i ==0 : left_up =0
            else: left_up = dp[i-1][j-1]
            
            if i == n-1: left_down = 0
            else: left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
result = 0
for i in range(n):
    result = max(result, dp[i][m - 1])
print(result)
"""

# 병사 배치하기
"""
n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1]*n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]
            dp[i] = max(dp[i], dp[j]+1)
            
print(n - max(dp))

# LIS문제 위에꺼는 n^2 ... https://rebro.kr/33 <- 요건 O(nlogN) 짜리
"""
