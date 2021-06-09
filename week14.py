# 14주차 기타 알고리즘

# 소수 판별 알고리즘
"""
def is_prime_number(x):
    for i in range(2, x):
        if x % i ==0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))
"""

# 소수 판별 개선버전 ( O( N ^ (1/2) ) )
"""
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i ==0:
            return False
    return True
"""

# 에라토스테네스의 체 ( O(Nlog(logN)) 빠르지만 공간복잡도 너무큼 )
"""
import math

n = 1000

array = [ True for i in range(n+1) ]

for i in range(2, int(math.sqrt(n))+1 ):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j = j+1
            
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')
"""

# 특정한 합을 가지는 부분 연속 수열 찾기 ( 부분합을 사용 )
"""
n = 5
m = 5
data = [1, 2, 3, 4, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum = interval_sum + data[end]
        end = end +1
        
        if interval_sum == m:
            count = count + 1
        interval_sum = interval_sum - data[start]
        
print(count)
"""

# 구간 합 빠르게 계산하기 ( N개의 정수 M개의 쿼리 O( N+M ) )
"""
n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]

for i in data:
    sum_value = sum+value +i
    prefix_sum.append(sum_value)
    
left = 3
right = 4
print(prefix_sum[right] = prefix_sum[left -1])
"""

