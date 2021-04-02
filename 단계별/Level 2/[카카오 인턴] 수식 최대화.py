from collections import deque


def get_op_priority(op):
    op_priority_list = []
    qu = deque()
    qu.extend(op)
    while qu:
        cur_op = qu.popleft()
        if len(cur_op) == len(op):
            op_priority_list.append(cur_op)
        for new_op in op:
            if new_op not in cur_op:
                qu.append(cur_op + new_op)

    return op_priority_list


def calculate(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    else:
        return num1 * num2


def apply_priority(op_priority, explist):
    exp = explist.copy()
    while len(exp) > 1:
        for i in range(len(op_priority)):
            op = op_priority[i]
            j = 1  # 어차피 explist[0]는 숫자
            while j < len(exp):
                if exp[j] == op:
                    exp[j] = calculate(exp[j - 1], op, exp[j + 1])
                    del exp[j + 1]
                    del exp[j - 1]
                else:
                    j += 1

    return abs(exp[0])


def solution(expression):
    # step 1) expression 분리
    explist = []
    opset = set()
    num = ''
    for i in range(len(expression)):
        if expression[i] in '-+*':
            opset.add(expression[i])
            explist.append(int(num))
            explist.append(expression[i])
            num = ''
        else:
            num += expression[i]
    explist.append(int(num))

    # step 2) 연산자 우선순위 경우의 수
    op_priority_list = get_op_priority(list(opset))

    # step 3) 연산자 우선순위별 결과값
    max_result = 0
    for op_priority in op_priority_list:
        result = apply_priority(op_priority, explist)
        max_result = max(max_result, result)

    return max_result

