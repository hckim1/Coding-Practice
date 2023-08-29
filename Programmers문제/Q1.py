
# 짝수와 홀수
# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
# 제한 조건
# num은 int 범위의 정수입니다.
# 0은 짝수입니다.

#
# def solution(num):
#     # 입력된 숫자가 짝수인지 홀수인지 판별하여 결과를 반환하는 함수입니다.
#     if num % 2 == 0:
#         return "Even"  # 짝수인 경우 "Even"을 반환합니다.
#     else:
#         return "Odd"  # 홀수인 경우 "Odd"를 반환합니다.
#
#
# # 사용자로부터 정수 입력 받기
# user_input = input("정수를 입력하세요: ")
# try:
#     # 입력 받은 값을 정수로 변환하여 num 변수에 저장합니다.
#     num = int(user_input)
#
#     # 변환된 정수 num을 solution 함수에 전달하여 짝수인지 홀수인지 판별하고 결과를 result 변수에 저장합니다.
#     result = solution(num)
#
#     # 계산된 결과를 출력합니다.
#     print(result)
# except ValueError:
#     # 입력 값이 유효한 정수가 아닌 경우 에러 메시지를 출력합니다.
#     print("유효한 정수를 입력해주세요.")


def solution(num):
    if num & 2 == 0:
        return "짝수"
    else:
        return "홀수"

user = input("정수를 입력")
num = int(user)
result = solution(num)

print(f"{user}은 {result}이다")
