# 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
# 예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.

def solution(s):
    return int(s)

user_input = input("부호와 숫자로만 이루어진 문자열을 입력하세요: ")
result = solution(user_input)
print(f"입력한 문자열을 숫자로 변환한 결과: {result}")