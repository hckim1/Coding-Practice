# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고,
# n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

def solution(n):
# n의 제곱근 구하기(루트 씌우면 됨)
    n = n ** (0.5)
# n이 정수면 n+1의 제곱 리턴
    if n % 1 == 0:
        return (n + 1) ** 2
# 정수가 아닐경우 -1 리턴
    return -1

user_input = int(input("양의 정수를 입력하세요: "))  # 사용자로부터 양의 정수 입력 받기
result = solution(user_input)  # solution 함수 호출하여 결과 계산

if result != -1:
    print(f"{user_input}은 양의 정수 {int(user_input ** 0.5)}의 제곱이므로, 결과는 {result}입니다.")
else:
    print(f"{user_input}은 양의 정수의 제곱이 아니므로, 결과는 {result}입니다.")