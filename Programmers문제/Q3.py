# 자릿수 더하기
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
#
# 제한사항
# N의 범위 : 100,000,000 이하의 자연수

# def solution(n):
#     # 자연수 n을 문자열로 변환하고 각 자릿수를 문자열 리스트로 저장합니다.
#     digits = list(str(n))
#
#     # 각 자릿수를 정수로 변환하고 합을 계산합니다.
#     digit_sum = sum(int(digit) for digit in digits)
#       #리스트 내 각 숫자 자릿수를 정수로 변환해서 모두 더한 값을 digits_sum 변수에 저장
#     # 계산된 자릿수 합을 반환합니다.
#     return digit_sum
#
#
# # 사용자로부터 자연수 입력 받기
# user_input = input("자연수를 입력하세요: ")
# try:
#     # 입력 받은 값을 정수로 변환하여 num 변수에 저장합니다.
#     num = int(user_input)
#
#     # 변환된 정수 num을 solution 함수에 전달하여 각 자릿수의 합을 계산하고 결과를 result 변수에 저장합니다.
#     result = solution(num)
#
#     # 결과를 출력합니다.
#     print("각 자릿수의 합:", result)
# except ValueError:
#     # 입력 값이 유효한 자연수가 아닌 경우 에러 메시지를 출력합니다.
#     print("유효한 자연수를 입력해주세요.")


def solution(n):
    digits = list(str(n))

    digit_sum = sum(int(digit) for digit in digits)
    return digit_sum

user_print = int(input("put "))
result = solution(user_print)
print(result)