# 2주차 그리디

#  거스름 돈
"""
n = 1260
count = 0

array = [500,100,50,10] # 동전의 종류

for coin in array:
    count = count+(n // coin)
    n = n%coin

print(count)

화패의 종류가 K 라고 할때 , 소스코드의 시간 복잡도는 O(K)
시간복잡도는 거슬러줘야 하는 금액과는 무관 , 동전의 총 종류에만 영향을 받음
"""

# 배낭 문제
"""
cargo=[(4,12),(2,1),(10,4),(1,1),(2,2)] # 앞 가치 , 뒤 무게

def fractional_knapsack(cargo):
    capacity=15
    pack=[]
    for c in cargo:
        pack.append((c[0]/c[1] , c[0] , c[1]))
    pack.sort(reverse=True) # 첫번째 인자 순으로 정렬
    
    total_value: float = 0
    for p in pack:
        if capacity - p[2] >= 0: # 아직 넣을 수 있으면
            capacity = capacity - p[2]
            total_value = total_value + p[1]
        else: # 넣지 못한다면
            fraction = capacity / p[2] # 남은 용량을 해당 무게로 나눠서 나논 결과값을
            total_value = total_value+ p[1]*fraction # 최종 가치에 곱한것을 더하고
            break # 종료
    
    return total_value
    
https://www.acmicpc.net/source/29542793  << DP 평범한 배낭 C++
"""

# 1이 될 때 까지
"""
n,k = map(int,input().split()) # 25 / 3

result=0

while True:
    target = (n//k) * k 
    result = result + (n-target)
    n = target
    if n < k:
        break
        
    result += 1
    n = n//k
    
result = result + (n-1)
print(result)
"""

# 곱하기 혹은 더하기
"""
data = input() # 문자열 형태로 입력

result = int(data[0]) # 첫번째 수를 int 로

for i in range(1,len(data)): # 첫번째 이후부터 끝까지
    num = int(data[i]) # 해당 데이터를 꺼내서 int로 변형
    if num <= 1 or result <= 1: # 수가 1보다 작거나 결과 값이 1보다 작으면
        result += num # 해당 수는 곱하지말고 더하기
    else:
        result *= num # 나머지는 곱하기

print(result)
"""

# 모험가 길드
"""
n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 # 총 그룹 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count = count +1
    if count >= i:
    result = result+1
    count = 0
    
print(result)
"""
