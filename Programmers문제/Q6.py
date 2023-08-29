# 함수 solution은 정수 x와 자연수 n을 입력 받아,
# x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
# 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.


# def solution(x, n):
#     # 리스트 안에 x * 1~n 나열하기
#     result = [x * i for i in range(1, n + 1)]
#
#     return result

# 주어진 x부터 시작해서 x씩 증가하는 숫자를 n개 지니는 리스트를 생성하는 코드입니다.
# x와 n을 이용하여 리스트 내포(comprehension) 방식을 사용하여 리스트를 생성하고 반환합니다.
# 주어진 조건에 맞게 정확히 동작하는 코드입니다.
#
# 이 코드 역시 주어진 문제의 조건에 따라 원하는 결과를 얻을 수 있는 좋은 방식입니다.


def solution(x, n):
    # 결과를 저장할 리스트 초기화
    result = []

    # 1부터 n까지 반복하여 리스트에 x * i 값 추가
    for i in range(1, n + 1):
        result.append(x * i)

    # 결과 리스트 반환
    return result

user_input = input("x와 n을 공백으로 구분하여 입력하세요: ")
x, n = map(int, user_input.split())  # 입력된 문자열을 정수로 변환

result = solution(x, n)
print(result)


# solution 함수는 주어진 x와 n을 이용하여 x부터 시작해
# x씩 증가하는 숫자를 n개 지니는 리스트를 반환하는 함수입니다.
#
# result 리스트는 결과를 저장할 빈 리스트로 초기화됩니다.
#
# for 루프를 통해 1부터 n까지의 숫자 범위를 반복합니다.
#
# x * i 값은 주어진 x를 i번 곱한 값을 나타냅니다. 이 값을 result 리스트에 추가합니다.
#
# return result를 통해 계산된 결과 리스트를 반환합니다.
