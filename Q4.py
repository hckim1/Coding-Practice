#약수의 합
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
#
# 제한 사항
# n은 0 이상 3000이하인 정수입니다.


def solution(n):
    # 약수의 합을 저장할 변수를 초기화합니다.
    answer = 0

    # 1부터 n까지의 숫자를 순회합니다.
    for i in range(1, n + 1):
        # 만약 n을 i로 나눴을 때 나머지가 0이면, i는 n의 약수입니다.
        if n % i == 0:
            # 약수를 약수의 합에 더합니다.
            answer += i

    # 계산된 약수의 합을 반환합니다.
    return answer


# 사용자로부터 정수 입력 받기
user_input = input("정수를 입력하세요: ")
try:
    # 입력 받은 값을 정수로 변환하여 num 변수에 저장합니다.
    num = int(user_input)

    # 변환된 정수 num을 solution 함수에 전달하여 약수의 합을 계산하고 결과를 result 변수에 저장합니다.
    result = solution(num)

    # 계산된 약수의 합을 출력합니다.
    print("약수의 합:", result)
except ValueError:
    # 입력 값이 유효한 정수가 아닌 경우 에러 메시지를 출력합니다.
    print("유효한 정수를 입력해주세요.")