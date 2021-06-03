# 8주차 정렬

# 선택정렬 O(n^2)
"""
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index] , array[i]

print(array)
"""

# 삽입정렬 O(n^2) 최선이면 O(N)
"""
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i, 0 , -1): # reverse 로
        if array[i] < array[j-1] # 일반적으로 오름차순 정렬이므로
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
            
print(array)
# https://gmlwjd9405.github.io/2018/05/06/algorithm-insertion-sort.html
"""

# 퀵정렬 O(NlogN) 최악이면 O(N^2)
"""
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start >= end:
        return
        
    pivot = start
    left = start + 1 # pivot 보다 큰 데이터 탐색
    right = end # pivot 보다 작은 데이터 탐색
    
    while left <= right:
        while left <= end and array[left] <= array[pivot]: # pivot 보다 큰 데이터 탐색
            left = left+1
        while right > start and array[right] >= array[pivot]: # pivot 보다 작은 데이터 탐색
            right = right -1 
        if left > right: # 탐색을 못 하였을경우
            array[right], array[pivot] = array[pivot], array[right]
        else: # 탐색시 
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right -1)
    quick_sort(array, right +1, end)

quick_sort(array, 0, len(array)-1)
print(array)
"""

# 계수정렬 O(N + K) ㅈㄴ 빠르지만 공간복잡도 O(N + K) 고려
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] = count[array[i]] + 1
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
"""

# 안테나
"""
n = int(input())
data = list(map(int, input().split()))
data.sort() # 정확히 가운데에 있을때 최소값

print(data[(n-1) // 2])
"""

# 두 배열의 원소 교체
"""
n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(rever=True)

for i in range(k)
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break
    
print(sum(a))
"""


