# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아,
# "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요.
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.


def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

# 실행을 위한 테스트코드입니다.
print(findKim(["Kim"]))  # "김서방은 2에 있다"

# seoul.index('Kim')는 리스트 seoul에서 "Kim"의 인덱스를 반환합니다. 이렇게 하면 "Kim"의 위치를 정수로 얻을 수 있습니다.
#
# "김서방은 {}에 있다".format(seoul.index('Kim'))는 문자열 포맷팅을 사용하여 "김서방은 x에 있다" 문자열을 생성합니다. {} 안에 seoul.index('Kim') 값이 들어가게 됩니다.
#
# 생성된 문자열을 반환합니다.
#
# 주어진 함수는 배열 seoul에서 "Kim"의 위치를 찾아 "김서방은 x에 있다"라는 문자열을 반환합니다. 이러한 방식도 문제를 해결하는데 효과적입니다.