# 9주차 이진탐색

# 파이썬 이진탐색 라이브러리
"""
bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
bisect_right(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x)) # 2
print(bisect_right(a,x)) # 4
"""

# 값이 특정 범위에 속하는 데이터 개수 구하기
"""
from bisect import bisect_left, bisect_right:

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    
    return right_index - left_index
    
a = [1, 2, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))
"""

# 떡볶이 떡 만들기
"""
n, m = list(map(int,input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0 

while True:
    total = 0
    mid = (start+end) // 2
    for x in array:
        if x > mid:
            total = total + x - mid
            
    if total < m :
        end = mid-1
    else:
        result = mid
        start = mid +1
"""

# 정렬된 배열에서 특정 수의 개수 구하기: O(logN) 즉 선형탐색으로는 시간 초과
"""
데이터가 정렬되어 있으므로 이진탐색 가능
첫번째 등장하는 위치와 마지막 등장하는 위치를 찾아서 구할 수 있음

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right-value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index
    
n, m = map(int ,input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count ==0 :
    print(-1)
else:
    print(count)
"""

# 동전 계단쌓기: O(logN)
"""
def arrageCoins(n):
    left, right = 0, n
    while left <= right:
        k = (right + left) // 2
        current = k * (k + 1) // 2
        if current == n:
            return k
        if n < current:
            right = k - 1
        else:
            left = k + 1
    return right

n = 8

answer = arrangeCoins(n)
print(answer)
"""

# 산꼭대기 찾기: O(logN)
"""
def peakIndexInMountainArray(lst):
    low, high = 0, len(lst)-1
    while low < high:
        mi = int((low + high) // 2)
        if lst[mi] < lst[mi + 1]:
            low = mi + 1
        else:
            high = mi
    return low
    
lst = [3, 4, 5, 1]

answer = peakIndexInMountainArray(lst)
print(answer)
"""

