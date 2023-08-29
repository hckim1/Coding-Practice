# 연결 리스트 구현과 추가: 연결 리스트를 구현하고, 값을 추가하는 append 메서드를 작성해보세요.
#
# 연결 리스트 역순: 주어진 연결 리스트를 역순으로 만드는 방법을 설명하거나 코드로 작성해보세요.
#
# 두 연결 리스트 병합: 두 개의 정렬된 연결 리스트가 주어졌을 때, 두 리스트를 병합하여 정렬된 하나의 연결 리스트로 만드는 방법을 설명하거나 코드로 작성해보세요.
#
# 연결 리스트 중간 노드 찾기: 연결 리스트의 중간 노드를 찾는 방법을 설명하거나 코드로 작성해보세요.
#
# 연결 리스트 사이클 검사: 연결 리스트에 사이클이 있는지 검사하는 방법을 설명하거나 코드로 작성해보세요.
#
# 연결 리스트 문제 해결: 예를 들어, 연결 리스트에서 중복된 값을 제거하는 방법을 설명하거나 코드로 작성해보세요.
#
# 연결 리스트 활용: 주어진 문제를 해결하는 과정에서 연결 리스트를 활용하는 방법을 설명하거나 코드로 작성해보세요. (예: 두 수를 더하는 문제 등)

# 단일 연결 리스트의 노드 클래스 정의
class ListNode:
    def __init__(self, val=0, next=None):
        """
        노드 클래스의 생성자입니다. 각 노드는 값(val)과 다음 노드를 가리키는 포인터(next)를 갖습니다.
        :param val: 노드의 값
        :param next: 다음 노드를 가리키는 포인터
        """
        self.val = val
        self.next = next

# 연결 리스트 클래스 정의
class LinkedList:
    def __init__(self):
        """
        연결 리스트 클래스의 생성자입니다. 초기에 헤드 노드를 None으로 설정합니다.
        """
        self.head = None

    # 1. 연결 리스트에 값을 추가하는 메서드
    def append(self, val):
        """
        연결 리스트에 값을 추가하는 메서드입니다.
        :param val: 추가할 값
        """
        if not self.head:
            self.head = ListNode(val)  # 빈 리스트일 경우 새 노드를 헤드로 설정
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val)  # 마지막 노드의 다음에 새 노드 추가

    # 2. 연결 리스트를 역순으로 변경하는 메서드
    def reverse(self):
        """
        연결 리스트를 역순으로 변경하는 메서드입니다.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev  # 현재 노드의 next를 이전 노드로 설정
            prev = current
            current = next_node
        self.head = prev  # 헤드를 역순으로 된 첫 번째 노드로 설정

    # 3. 두 정렬된 연결 리스트를 병합하는 메서드
    def merge(self, other_list):
        """
        두 정렬된 연결 리스트를 병합하는 메서드입니다.
        :param other_list: 병합할 또 다른 연결 리스트
        :return: 병합한 연결 리스트
        """
        merged = LinkedList()  # 두 연결 리스트를 병합한 결과를 담을 새로운 연결 리스트 생성
        current_self = self.head
        current_other = other_list.head
        while current_self and current_other:
            if current_self.val < current_other.val:
                merged.append(current_self.val)  # 작은 값을 가진 노드를 추가하고
                current_self = current_self.next
            else:
                merged.append(current_other.val)  # 작은 값을 가진 노드를 추가하고
                current_other = current_other.next

        while current_self:
            merged.append(current_self.val)  # 남은 노드들을 추가
            current_self = current_self.next

        while current_other:
            merged.append(current_other.val)  # 남은 노드들을 추가
            current_other = current_other.next

        return merged

    # 4. 연결 리스트의 중간 노드 값을 찾는 메서드
    def find_middle(self):
        """
        연결 리스트의 중간 노드 값을 찾는 메서드입니다.
        :return: 중간 노드의 값
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next  # slow는 한 칸씩, fast는 두 칸씩 움직이며 중간 노드 찾음
            fast = fast.next.next
        return slow.val

    # 5. 연결 리스트에 사이클이 있는지 검사하는 메서드
    def has_cycle(self):
        """
        연결 리스트에 사이클이 있는지 검사하는 메서드입니다.
        :return: 사이클 여부 (True 또는 False)
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # slow와 fast가 만나면 사이클이 존재
                return True
        return False  # fast가 끝에 도달하면 사이클이 없음

# LinkedList 객체 생성
linked_list = LinkedList()

# 노드 추가
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# 링크드 리스트 역순으로 변경
linked_list.reverse()

# 두 연결 리스트 병합
another_list = LinkedList()
another_list.append(2)
another_list.append(4)
merged_list = linked_list.merge(another_list)

# 중간 노드 값 찾기
middle_value = linked_list.find_middle()

# 사이클 검사
has_cycle = linked_list.has_cycle()
