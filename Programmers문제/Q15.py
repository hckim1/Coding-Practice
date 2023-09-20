# 나누어 떨어지는 숫자 배열
# 문제 설명
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

#풀이 
# 주어진 리스트 arr의 요소 중에서 divisor로 나누어 떨어지는 요소들을 오름차순으로 정렬한 리스트를 반환

# 주어진 리스트 arr를 순회하며 다음 조건을 만족하는 요소들을 필터링
# - 현재 요소 n을 divisor로 나누었을 때 나머지가 0인 경우 (즉, 나누어 떨어지는 경우)
[n for n in arr if n % divisor == 0]

# 위 조건을 만족하는 요소들을 오름차순으로 정렬
sorted([n for n in arr if n % divisor == 0])

# 만약 정렬된 리스트가 비어있다면 (즉, 나누어 떨어지는 요소가 없다면),
# [-1]을 반환 이는 문제에서 정의한 만약 어떤 요소도 나누어 떨어지지 않는다면 -1을 포함한 리스트를 반환
or [-1]

# 정렬된 리스트가 비어있지 않다면, 정렬된 리스트를 반환
# 이 경우에는 나누어 떨어지는 요소들이 오름차순으로 정렬되어 반환

#1
def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]

#2
# 결과를 저장할 빈 리스트를 만듭니다.
answer = []

# 입력 리스트 arr를 순회하며 다음 조건을 만족하는 요소들을 찾는다
for i in arr:
    # 현재 요소 i를 divisor로 나누었을 때 나머지가 0인 경우 (즉, 나누어 떨어지는 경우)
    if i % divisor == 0:
        # 나누어 떨어지는 요소 i를 결과 리스트 answer에 추가
        answer.append(i)

# 나누어 떨어지는 요소들이 저장된 answer 리스트를 정렬
sorted_answer = list(sorted(answer))

# 만약 정렬된 리스트가 비어있다면 (즉, 나누어 떨어지는 요소가 없다면),
# answer에 -1을 포함한 리스트를 할당
if len(sorted_answer) == 0:
    sorted_answer = [-1]

# 정렬된 결과 리스트를 반환
return sorted_answer


