# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.


def solution(n):
    result = [int(i) for i in reversed(str(n))]
    #입력한 숫자를 문자열로 바꾼후, 문자들을 역순으로 뒤집기
     #그리고 역순으로 뒤집힌 문자들을 하나씩 꺼내서 정수로 바꾸기
     return result

user_input = int(input("숫자를 입력하세요: "))  # 입력을 정수로 변환
result = solution(user_input)
print(f"{user_input}을 거꾸로 하면 {result}다")