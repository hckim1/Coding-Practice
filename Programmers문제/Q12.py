# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

def solution(a, b):
    # a와 b 중 작은 수를 start로, 큰 수를 end로 설정합니다.
    start = min(a, b)
    end = max(a, b)

    # start부터 end까지의 모든 정수의 합을 구합니다.
    total_sum = sum(range(start, end + 1))

    return total_sum

# 함수 solution(a, b)가 호출되면 두 개의 정수 a와 b를 입력으로 받습니다.
#
# start 변수에 min(a, b)를 할당합니다. min(a, b)는 a와 b 중에서 작은 값을 선택하는 함수입니다.
# 이렇게 함으로써 start에는 두 수 중 작은 값이 들어가게 됩니다.
#
# end 변수에 max(a, b)를 할당합니다. max(a, b)는 a와 b 중에서 큰 값을 선택하는 함수입니다.
# 이렇게 함으로써 end에는 두 수 중 큰 값이 들어가게 됩니다.
#
# range(start, end + 1)은 start부터 end까지의 모든 정수를 생성하는 함수입니다.
# range() 함수는 마지막 값에 도달하기 전까지의 정수를 생성합니다. 따라서 end + 1을 사용하여 end를 포함한 범위까지 생성하도록 합니다.
#
# sum(range(start, end + 1))은 생성된 정수의 합을 구하는 함수입니다. 이를 통해 start부터 end까지의 모든 정수의 합을 계산합니다.
#
# 마지막으로, 계산된 총 합인 total_sum을 반환합니다.
#
# 이 함수는 주어진 두 정수 a와 b 사이의 모든 정수의 합을 계산하여 반환합니다. a와 b의 순서에 관계없이 동작하며, 범위는 start와 end로 설정됩니다.