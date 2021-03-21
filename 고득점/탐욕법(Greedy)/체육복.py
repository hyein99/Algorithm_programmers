def solution(n, lost, reserve):
    # lost이면서 reserve인 학생 제거
    L = set(lost)-set(reserve)
    R = set(reserve)-set(lost)

    for r in R:     # 여벌 체육복을 가져온 학생
        if r-1 in L:
            L.remove(r-1)
        elif r+1 in L:
            L.remove(r+1)

    # 체육복을 갖게 된 학생 수 리턴
    return n - len(L)


def solution2(n, lost, reserve):
    L = sorted(list(set(lost)-set(reserve)))
    R = sorted(list(set(reserve)-set(lost)))

    cnt, i, j = 0, 0, 0   # 체육복 못빌린 학생수, lost index, reserve index
    while i < len(L) and j < len(R):
        # Reserve를 기준으로 Lost가 체육복을 빌릴 수 있는지 판단
        # case 1: 빌려줄 수 있는 범위 최소값보다 작은 학생 있으면 못빌리는 학생으로 분류
        if R[j] - 1 > L[i]:
            cnt += 1
            i += 1
        # case 2: 빌려줄 수 있는 범위보다 크면 다음 Reserve 학생으로 넘어감
        elif R[j] + 1 < L[i]:
            j += 1
        # case 3: R이 L에게 빌려줄 수 있는 경우
        else:
            i += 1
            j += 1
    cnt += len(L) - i # 남은 체육복 못 빌린 애들 추가 해줌

    return n - cnt

# print(solution(n=5, lost=[2,4], reserve=[1,3,5]))
# print(solution(n=5, lost=[2,4], reserve=[3]))
# print(solution2(n=7, lost=[1,2,3,4,5,6,7], reserve=[1,2,3]))
print(solution2(n=5, lost=[1,2,4,5], reserve=[2,3,4]))