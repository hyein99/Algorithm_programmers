from collections import defaultdict


def solution(orders, course):
    # order에서 legth 길이의 부분집합을 찾는 함수
    def count_orders(sub, start, length, order):
        # 종료조건
        if len(order) < length:
            return
        if len(sub) == length:
            order_dict[sub] += 1
            return

        for i in range(start, len(order)):
            count_orders(sub + order[i], i + 1, length, order)
        return

    # 각 order의 부분집합을 딕셔너리에 저장
    order_dict = defaultdict(int)
    for i in range(len(orders)):
        order = sorted(list(orders[i]))
        for j in range(2, len(order) + 1):
            count_orders('', 0, j, order)

    # course[i]를 길이로 가지는 order 최대값 구하기
    course_cnt = defaultdict(int)
    for order in order_dict:
        length = len(order)
        if length in course and order_dict[order] >= 2:
            course_cnt[length] = max(course_cnt[length], order_dict[order])

    # course에 해당하는 order answer에 저장
    answer = []
    for order in order_dict:
        if order_dict[order] == course_cnt[len(order)]:
            answer.append(order)
    answer.sort()

    return answer