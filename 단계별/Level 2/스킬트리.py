def solution(skill, skill_trees):
    def is_stree(stree):
        cnt = 1
        for s in stree:
            if s in skill_order:  # 선행 skill 순서가 있는 skill tree
                if skill_order[s] != cnt:
                    return False
                cnt += 1

        return True

    # step 1. skill의 순서를 나타내는 그래프 생성
    skill_order = dict()
    order = 1
    for s in skill:
        skill_order[s] = order
        order += 1

    # step 2. skill_tree 탐색
    cnt = 0
    for stree in skill_trees:
        if is_stree(stree):
            cnt += 1

    return cnt